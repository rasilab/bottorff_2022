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
		trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3}
		trailing_ssu_product_args = {'asite': 2, 'hit3': None}
		sb.Rule(f'recycle_from_trailing_collision_{pos}',
				ssu(**ssu_reactant_args) % ssu(**trailing_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
				ssu(**ssu_product_args) + ssu(**trailing_ssu_product_args) % mrna(**mrna_product_args),
				k)

	# recycle out of a collision with a leading scanning ribosome
	mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
	mrna_product_args = copy.deepcopy(mrna_product_temp)

	if pos < model.l_mrna - model.l_ssu:
		mrna_reactant_args[f'nt{pos + model.l_ssu}'] = 2
		mrna_product_args[f'nt{pos + model.l_ssu}'] = 2
		ssu_reactant_args['hit5'] = None
		ssu_reactant_args['hit3'] = 3
		leading_ssu_reactant_args = {'asite': 2, 'hit5': 3}
		leading_ssu_product_args = {'asite': 2, 'hit5': None}
		sb.Rule(f'recycle_from_leading_collision_{pos}',
				ssu(**ssu_reactant_args) % ssu(**leading_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
				ssu(**ssu_product_args) + ssu(**leading_ssu_product_args) % mrna(**mrna_product_args),
				k)

	# recycle out of a collision with leading and trailing scanning ribosomes
	mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
	mrna_product_args = copy.deepcopy(mrna_product_temp)

	if ((pos < model.l_mrna - model.l_ssu) and (pos > model.l_ssu - 1)):
		mrna_reactant_args[f'nt{pos - model.l_ssu}'] = 2
		mrna_product_args[f'nt{pos - model.l_ssu}'] = 2
		mrna_reactant_args[f'nt{pos + model.l_ssu}'] = 4
		mrna_product_args[f'nt{pos + model.l_ssu}'] = 4
		ssu_reactant_args['hit5'] = 3
		ssu_reactant_args['hit3'] = 5
		trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3}
		trailing_ssu_product_args = {'asite': 2, 'hit3': None}
		leading_ssu_reactant_args = {'asite': 4, 'hit5': 5}
		leading_ssu_product_args = {'asite': 4, 'hit5': None}
		sb.Rule(f'recycle_from_both_collision_{pos}',
				ssu(**ssu_reactant_args) % ssu(**trailing_ssu_reactant_args) % mrna(**mrna_reactant_args) % ssu(**leading_ssu_reactant_args) >>
				ssu(**ssu_product_args) + ssu(**trailing_ssu_product_args) % mrna(**mrna_product_args) % ssu(**leading_ssu_product_args)  ,
				k)
