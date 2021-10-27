import pysb as sb
import copy

def terminate(model, ssu, lsu, mrna, pos, k):
	"""Terminate at position pos by leaving of the large subunit.
	Ribosome can be not hit or hit from 5' by a trailing scanning or elongating ribosome.
	The small subunit is recycled separately to allow for re-initiation after binding ternary complex.
	"""

	mrna_reactant_args = {f'nt{pos}': 1}
	mrna_product_args = {f'nt{pos}': 1}

	ssu_reactant_args = {'asite': 1, 'isbi': 8, 'terminating': 'no'}
	ssu_product_args = {'asite': 1, 'isbi': None, 'terminating': 'yes'}

	lsu_reactant_args = {'isbi': 8}
	lsu_product_args = {'isbi': None}

	sb.Rule(f'terminate_{pos}',
			ssu(**ssu_reactant_args) % lsu(**lsu_reactant_args) % mrna(**mrna_reactant_args) >>
			lsu(**lsu_product_args) +
			ssu(**ssu_product_args) % mrna(**mrna_product_args),
			k)

def recycle_terminated_ssu(model, ssu, lsu, mrna, pos, k):
	"""An ssu on mRNA after termination without large subunit is recycled to the free ssu pool.
	If this does not occur efficiently, then the ssu continues scanning, and
	can elongate again after binding a TC
	"""
	ssu_reactant_args = {'asite': 1, 'hit5': None, 'hit3': None,
							'isbi': None, 'tcsite': None, 'terminating': 'yes'}
	ssu_product_args = {'asite': None, 'hit5': None, 'hit3': None,
						'isbi': None, 'tcsite': None, 'terminating': 'no'}
	mrna_reactant_args = {f'nt{pos}': 1}
	mrna_product_args = {f'nt{pos}': None}

	# if ribosome terminates within a footprint from the 5' end, cap is free to bind another PIC
	if pos < model.l_ssu:
		mrna_reactant_args['end5'] = 'blocked'
		mrna_product_args['end5'] = 'free'

	sb.Rule(f'recycle_{pos}',
			ssu(**ssu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) + mrna(**mrna_product_args),
			k)

	# create temporary copy of mrna_reactant and mrna_product args for different conditions
	mrna_reactant_temp = copy.deepcopy(mrna_reactant_args)
	mrna_product_temp = copy.deepcopy(mrna_product_args)

	# recycle out of a collision with a trailing scanning ribosome
	mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
	mrna_product_args = copy.deepcopy(mrna_product_temp)

	if pos > model.l_ssu - 1:
		mrna_reactant_args[f'nt{pos - model.l_ssu}'] = 2
		mrna_product_args[f'nt{pos - model.l_ssu}'] = 2
		ssu_reactant_args['hit5'] = 3
		trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3, 'isbi': None}
		trailing_ssu_product_args = {
			'asite': 2, 'hit3': None, 'isbi': None}
		sb.Rule(f'recycle_from_scan_collision_{pos}',
				ssu(**ssu_reactant_args) % ssu(**trailing_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
				ssu(**ssu_product_args) + ssu(**
												trailing_ssu_product_args) % mrna(**mrna_product_args),
				k)

	# recycle out of a collision with a trailing elongating ribosome
	mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
	mrna_product_args = copy.deepcopy(mrna_product_temp)
	if pos > model.l_ribo - 1:
		mrna_reactant_args[f'nt{pos - model.l_ribo}'] = 2
		mrna_product_args[f'nt{pos - model.l_ribo}'] = 2
		ssu_reactant_args['hit5'] = 3
		trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3, 'isbi': 6}
		trailing_ssu_product_args = {'asite': 2, 'hit3': None, 'isbi': 6}
		trailing_lsu_reactant_args = {'isbi': 6}
		trailing_lsu_product_args = {'isbi': 6}
		sb.Rule(f'recycle_from_elongation_collision_{pos}',
				ssu(**ssu_reactant_args) % ssu(**trailing_ssu_reactant_args) % lsu(**trailing_lsu_reactant_args) % mrna(**mrna_reactant_args) >>
				ssu(**ssu_product_args) + ssu(**trailing_ssu_product_args) % lsu(**
																					trailing_lsu_product_args) % mrna(**mrna_product_args),
				k)
