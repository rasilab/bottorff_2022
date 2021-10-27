import pysb as sb

def collide_upon_elongation(model,ssu, lsu, mrna, pos, k):
	"""The 80S at pos collides with a scanning or elongating ribosome at pos + l_ribo 
	because its translocation is blocked.
	"""

	mrna_reactant_args = {f'nt{pos}': 1, f'nt{pos + model.l_ribo}': 2}
	mrna_product_args = {f'nt{pos}': 1, f'nt{pos + model.l_ribo}': 2}

	ssu_reactant_args = {'asite': 1, 'hit3': None, 'isbi': 8}
	ssu_product_args = {'asite': 1, 'hit3': 3, 'isbi': 8}

	lsu_reactant_args = {'isbi': 8}
	lsu_product_args = {'isbi': 8}

	leading_ssu_reactant_args = {'asite': 2, 'hit5': None}
	leading_ssu_product_args = {'asite': 2, 'hit5': 3}

	sb.Rule(f'collide_upon_elongation_{pos}',
			ssu(**ssu_reactant_args) % lsu(**lsu_reactant_args) % ssu(**leading_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) % lsu(**lsu_product_args) % ssu(**
																	leading_ssu_product_args) % mrna(**mrna_product_args),
			k)

def collide_upon_scanning(model, ssu, lsu, mrna, pos, k):
	"""The PIC at pos collides with a scanning or elongating ribosome at pos + l_ssu
	because its scanning is blocked.
	"""

	mrna_reactant_args = {f'nt{pos}': 1, f'nt{pos + model.l_ssu}': 2}
	mrna_product_args = {f'nt{pos}': 1, f'nt{pos + model.l_ssu}': 2}

	ssu_reactant_args = {'asite': 1, 'hit3': None, 'isbi': None}
	ssu_product_args = {'asite': 1, 'hit3': 3, 'isbi': None}

	leading_ssu_reactant_args = {'asite': 2, 'hit5': None}
	leading_ssu_product_args = {'asite': 2, 'hit5': 3}

	sb.Rule(f'collide_upon_scanning_{pos}',
			ssu(**ssu_reactant_args) % ssu(**leading_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) % ssu(**
											leading_ssu_product_args) % mrna(**mrna_product_args),
			k)
