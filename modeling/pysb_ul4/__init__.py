"""Kinetic Model for Translational Regulation by Upstream Open Reading Frames

Ty Bottorff <tbottorff@fredhutch.org> 
Arvind Rasi Subramaniam <rasi@fredhutch.org> 
25 Aug 2021
"""

import pysb as sb
import copy
import yaml
from pkg_resources import resource_filename


class Model(sb.Model):
    """Class to model motion of ribosomes on mRNAs"""


    def set_params(self):
        """Read param names and values from the YAML file"""

        params_filepath = resource_filename(__name__, 'parameters.yaml')
        params_dict = yaml.safe_load(open(params_filepath, 'r'))
        for param in params_dict:
            sb.Parameter(param['param'], param['value'])


    def redefine_params(self, kwargs):
        """Redefine params using dictionary passed during model instantiation.
        """
        # reset parameters if passed as keyword during model instantiation
        for k, v in kwargs.items():
            try:
                self.parameters[k].value = v
            except KeyError:
                raise(f'Parameter {k} not in model {self.name}.')

        self.l_mrna = l_mrna.value
        self.l_ribo = l_ribo.value
        self.l_ssu = l_ssu.value


    def define_molecules(self):
        """Define the molecules and their internal states"""

        from . import molecules

        self.mrna = molecules.Mrna(self, 'mrna', l_mrna=int(self.l_mrna))
        self.ssu = molecules.SmallSubunit(self, 'ssu')
        self.lsu = molecules.LargeSubunit(self, 'lsu')
        self.tc = molecules.TernaryComplex(self, 'tc')


    def define_observables(self):
        """Define the observables that are tracked during the simulation.

        Not critical since we track all reactions
        """

        sb.Observable('n_mrna', self.mrna())
        #sb.Observable('n_tc', self.tc())

    def define_initial_conditions(self):
        """Define the initial number and states of molecules
        """

        if self.parameters['n_mrna_0'].value > 0:
            sb.Initial(self.mrna.get_initial_state(), n_mrna_0)

        sb.Initial(self.ssu.get_initial_state(), n_ssu_0)
        sb.Initial(self.lsu.get_initial_state(), n_lsu_0)
        sb.Initial(self.tc.get_initial_state(), n_tc_0)


    def __init__(self, **kwargs):
        """Instantiate an object of the class by calling above functions

        We use loops to define reactions that occur at multiple positions
        along mRNA. The individual reaction rules are defined further below.
        """

        # instantiate a pysb model object with default minimal structure
        super().__init__()

        # set parameters for the model to their default values
        self.set_params()

        # redefine parameters if they were passed during instantiation.
        # this is used to vary parameters of the model from an external script
        self.redefine_params(kwargs)

        # define molecules, their states and state values
        self.define_molecules()

        # define observables -- states that are tracked during the simulation
        self.define_observables()

        # define initial copy number of all molecular states
        self.define_initial_conditions()

        ###################################################################################
        # List all Reactions / Rules in the model with correct rates and location on mRNA #
        ###################################################################################

        from .reactions.translation_initiation import (
            bind_tc_free_ssu,
            bind_cap_pic,
            scan,
            scan_to_elongate,
        )
        # ternary complex binding to ssu
        bind_tc_free_ssu(tc=self.tc, ssu=self.ssu, k=k_ssu_tc_bind)

        # cap binding
        bind_cap_pic(tc=self.tc, ssu=self.ssu,
                     mrna=self.mrna, pos=0, k=k_cap_bind)

        # scanning from pos nt to nt + 1
        for nt in range(self.l_mrna - 1):
            scan(model, tc=self.tc, ssu=self.ssu, lsu=self.lsu,
                 mrna=self.mrna, pos=nt, k=k_scan)

        # transition from scanning to elongating ribosome.
        # this can occur only within 'l_mrna_capture' nt on either side of the start codon.
        # this is to mimic the idea of enhanced initiation of queued scanning ribosomes in ivanov 2018.
        # strictly speaking, this should occur only when the scanning ribosome is positioned at the exact A-site nucleotide.
        # the different k_start values mimic different intiation context strengths.
        start_and_rate = {
            uorf1_start.value: k_start_uorf1,
            uorf2_start.value: k_start_uorf2,
            uorf3_start.value: k_start_uorf3,
            orf_start.value: k_start_orf
        }
        for start, rate in start_and_rate.items():
            for nt in range(start - l_scan_capture.value, start + l_scan_capture.value + 1):
                scan_to_elongate(model, tc=self.tc, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, pos=nt,
                                 k=rate, newpos=start)

        from .reactions.translation_elongation import elongate

        # elongation
        for nt in (list(range(uorf1_start.value, uorf1_stop.value, 3)) +
                   list(range(uorf2_start.value, uorf2_stop.value, 3)) +
                   list(range(uorf3_start.value, uorf3_stop.value, 3)) +
                   list(range(orf_start.value, orf_stop.value, 3))):
            if n_stall.value != 1:
                raise("There can be only one stall in this model!")
            if nt == x_stall.value:
                elongate(model, self.ssu, self.lsu, self.mrna,
                         pos=nt, k=k_elong_stall)
            else:
                elongate(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, pos=nt, k=k_elong)

        from .reactions.translation_termination import (
            terminate,
            recycle_terminated_ssu,
        )

        # normal termination rate at uorf1, uorf3, main orf,
        # regulated termination rate at uorf2 of gp48.
        # note that recycling of ssu from mRNA to free pool is a separate step,
        # but recycling can occur only at stop codons. If a ssu escapes recycling by
        # scanning to the next nt, then it is as stable as a regular scanning ssu on mRNA
        # but still needs to bind TC in order to initiate at a start codon
        stop_and_rates = {
            uorf1_stop.value: (k_term, k_terminated_ssu_recycle),
            uorf2_stop.value: (k_term_uorf2, k_terminated_ssu_recycle_uorf2),
            uorf3_stop.value: (k_term_uorf3, k_terminated_ssu_recycle_uorf3),
            orf_stop.value: (k_term, k_terminated_ssu_recycle)
        }
        for nt, rates in stop_and_rates.items():
            terminate(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, pos=nt, k=rates[0])
            recycle_terminated_ssu(model, 
                ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, pos=nt, k=rates[1])

        from .reactions.ribosome_collision import (
            collide_upon_elongation,
            collide_upon_scanning,
        )

        # collisions
        stop_codons = [uorf1_stop.value, uorf2_stop.value,
                       uorf3_stop.value, orf_stop.value]
        for nt in range(self.l_mrna):
            # we avoid collisions by terminating 80S or 40S ribosomes with downstream 80S / 80S
            # to keep the kinetic definition of termination and recycling simple
            if nt in stop_codons:
                continue
            # scanning ribosomes collide at the rate at which they scan
            if nt < self.l_mrna - self.l_ssu:
                collide_upon_scanning(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, pos=nt, k=k_scan)
            # 80S ribosomes collide at the rate at which they elongate
            if nt < self.l_mrna - self.l_ribo:
                if nt == x_stall.value:
                    collide_upon_elongation(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, pos=nt, k=k_elong_stall)
                else:
                    collide_upon_elongation(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, pos=nt, k=k_elong)

        from .reactions.scanning_premature_termination import (
            scan_terminate_no_hit,
            scan_terminate_3_hit_elongating,
            scan_terminate_3_hit_scanning,
            scan_terminate_5_hit_elongating,
            scan_terminate_5_hit_scanning,
            scan_terminate_both_hit_elongating_elongating,
            scan_terminate_both_hit_elongating_scanning,
            scan_terminate_both_hit_scanning_elongating,
            scan_terminate_both_hit_scanning_scanning,
        )
        from .reactions.elongation_premature_termination import elong_preterm_no_hit

        # scanning ribosome terminates if it reaches the end of mRNA, either with or without 5' collision
        scan_terminate_no_hit(model, ssu=self.ssu, mrna=self.mrna, pos=self.l_mrna-1, k=k_scan_term_3_end)
        scan_terminate_5_hit_elongating(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, 
            pos=self.l_mrna-1, k=k_scan_term_3_end)
        scan_terminate_5_hit_scanning(model, ssu=self.ssu, mrna=self.mrna,
            pos=self.l_mrna-1, k=k_scan_term_3_end)

        # abortion by scanning and elongating ribosomes
        for nt in range(self.l_mrna - 1):
            scan_terminate_no_hit(model, ssu=self.ssu, mrna=self.mrna, 
            pos=nt, k=k_scan_term_no_hit)
            elong_preterm_no_hit(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, 
            pos=nt, k=k_elong_preterm_no_hit)

        # abortion by scanning ribosomes that hit a leading elongating ribosome
        for nt in range(self.l_mrna - self.l_ssu):
            scan_terminate_3_hit_elongating(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, 
                pos=nt, k=k_scan_term_3_hit_80s)

        # abortion by scanning ribosomes that hit a leading scanning ribosome
        for nt in range(self.l_mrna - self.l_ssu):
            scan_terminate_3_hit_scanning(model, ssu=self.ssu, mrna=self.mrna, 
            pos=nt, k=k_scan_term_3_hit_40s)

        # abortion by scanning ribosomes that are hit by a trailing elongating ribosome
        for nt in range(self.l_ribo, self.l_mrna - 1):
            scan_terminate_5_hit_elongating(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, 
                pos=nt, k=k_scan_term_5_hit_80s)

        # abortion by scanning ribosomes that are hit by a trailing scanning ribosome
        for nt in range(self.l_ssu, self.l_mrna - 1):
            scan_terminate_5_hit_scanning(model, ssu=self.ssu, mrna=self.mrna, 
            pos=nt, k=k_scan_term_5_hit_40s)

        # abortion by scanning ribosomes that hit a leading elongating ribosome and trailing elongating ribosome
        for nt in range(self.l_ribo, self.l_mrna - self.l_ssu):
            scan_terminate_both_hit_elongating_elongating(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, 
                pos=nt, k=k_scan_term_both_hit_80s_80s)

        # abortion by scanning ribosomes that hit a leading scanning ribosome and trailing elongating ribosome
        for nt in range(self.l_ribo, self.l_mrna - self.l_ssu):
            scan_terminate_both_hit_elongating_scanning(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, 
                pos=nt, k=k_scan_term_both_hit_80s_40s)

        # abortion by scanning ribosomes that hit a leading elongating ribosome and trailing scanning ribosome
        for nt in range(self.l_ssu, self.l_mrna - self.l_ssu):
            scan_terminate_both_hit_scanning_elongating(model, ssu=self.ssu, lsu=self.lsu, mrna=self.mrna, 
                pos=nt, k=k_scan_term_both_hit_40s_80s)

        # abortion by scanning ribosomes that hit a leading scanning ribosome and trailing scanning ribosome
        for nt in range(self.l_ssu, self.l_mrna - self.l_ssu):
            scan_terminate_both_hit_scanning_scanning(self, ssu=self.ssu, mrna=self.mrna, 
                pos=nt, k=k_scan_term_both_hit_40s_40s)
