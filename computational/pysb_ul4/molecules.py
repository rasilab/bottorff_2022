"""Defines all molecule types in the PySB model

Each molecule type is derived from the Monomer PySB class.
"""


import pysb as sb


class Mrna(sb.Monomer):
    """Model full mRNA molecule as a single monomer

    Sites:
        - end5: 
            - for binding of cap factors or for checking cap clearance
            - Site states:
                - free: ribosome can bind
                - blocked: ribosome cannot bind
        - nt: >
            multiple sites with one per nucleotide on mRNA.
            nucleotides are included/excluded from 5'UTR, CDS, 3'UTR depending
            on the specific model.
    """

    def __init__(self, model, name, l_mrna):

        self.l_mrna = l_mrna

        sites = ['end5']

        site_states = {
            'end5': ['free', 'blocked'],
        }

        for pos in range(l_mrna):
            sites.append(f'nt{pos}')

        super().__init__(name, sites=sites, site_states=site_states, _export=False)
        model.add_component(self)

    def get_initial_state(self):
        """Return initial state of the mRNA

        Sites:
            - end5: >
                free - no scanning or elongating ribosome on the mRNA at the 
                beginning of the simulation
            - nt: no ribosome bound to any of the nucleotides on the mRNA
        """

        initial = {'end5': 'free'}

        for pos in range(self.l_mrna):
            initial[f'nt{pos}'] = None

        return self(**initial)


class SmallSubunit(sb.Monomer):
    """Small Subunit of the ribosomes

    Sites:
        - asite: binds to the 'nt' site on the mRNA
        - hit3: interacts with the downstream ribosome
        - hit5: interacts with the upstream ribosome
        - isbi: interacts with the large ribosomal subunit
        - tcsite: interacts with the ternary complex
        - terminating: 
            - >
                whether the subunit is in a terminated conformation that allows
                recycling
            - Site states:
                - yes: recycling can occur
                - no: recycling cannot occur
    """

    def __init__(self, model, name):

        sites = ['asite', 'hit3', 'hit5', 'isbi', 'tcsite', 'terminating']

        site_states = {
            'terminating': ['yes', 'no']
        }

        super().__init__(name, sites=sites, site_states=site_states, _export=False)
        model.add_component(self)

    def get_initial_state(self):
        """Return initial state of the small subunit

        # small and large subunits are intially not bound to mRNAs or to each other
        # the ssu is not bound to tc either
        """
        initial = {
            'asite': None, 
            'hit3': None, 
            'hit5': None,
            'isbi': None,
            'tcsite': None,
            'terminating': 'no'
        }

        return self(**initial)



class LargeSubunit(sb.Monomer):
    """Large subunit of the ribosomes

    Sites:
        - isbi: interacts with the small ribosomal subunit
    """

    def __init__(self, model, name):

        sites = ['isbi']

        super().__init__(name, sites=sites, _export=False)
        model.add_component(self)

    def get_initial_state(self):
        """Return initial state of the large subunit

        # small and large subunits are intially not bound to mRNAs or to each other
        """
        initial = {'isbi': None}

        return self(**initial)

class TernaryComplex(sb.Monomer):
    """Ternary Complex composed of EIF2-GTP-tRNAMet

    Sites:
        - ssusite: interacts with the small ribosomal subunit
    """

    def __init__(self, model, name):

        sites = ['ssusite']

        super().__init__(name, sites=sites, _export=False)
        model.add_component(self)

    
    def get_initial_state(self):
        """Return initial state of the ternary complex

        # the ssu is not bound to tc
        """
        initial = {'ssusite': None}

        return self(**initial)
