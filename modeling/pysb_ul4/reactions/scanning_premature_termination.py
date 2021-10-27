import pysb as sb


def scan_terminate_no_hit(model, ssu, mrna, pos, k):
	"""Scanning ribosome leaves mRNA at position pos.
	PIC must not be hit r by a scanning or elongating ribosome.
        TC ejected
	"""

	mrna_reactant_args = {f'nt{pos}': 1}
	mrna_product_args = {f'nt{pos}': None}

        ssu_reactant_args = {'asite': 1, 'hit5': None, 'hit3': None, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': None, 'hit5': None, 'hit3': None, 'isbi': None, 'tcsite': None}

        tc_reactant_args = {'ssusite': 21}
        tc_product_args = {'ssusite': None}

	# if a scanning ribosome terminates within a footprint from the 5' end, cap is free to bind another PIC
	if pos < model.l_ssu:
		mrna_reactant_args['end5'] = 'blocked'
		mrna_product_args['end5'] = 'free'

	sb.Rule(f'scan_terminate_no_hit_{pos}',
			ssu(**ssu_reactant_args) % tc**(tc_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) + tc(**tc_product_args) + mrna(**mrna_product_args),
			k)


def scan_terminate_5_hit_scanning(model, ssu, mrna, pos, k):
	"""Scanning ribosome leaves mRNA at position pos after being hit by a trailing scanning ribosome.
        TC ejected
	"""

	mrna_reactant_args = {f'nt{pos}': 1, f'nt{pos - model.l_ssu}': 2}
	mrna_product_args = {f'nt{pos}': None, f'nt{pos - model.l_ssu}': 2}
        ssu_reactant_args = {'asite': 1, 'hit5': 3, 'hit3': None, 'isbi': None, 'tcsite': 21}}
        ssu_product_args = {'asite': None, 'hit5': None, 'hit3': None, 'isbi': None, 'tcsite': None}
	trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3, 'isbi': None}
	trailing_ssu_product_args = {'asite': 2, 'hit3': None, 'isbi': None}

        tc_reactant_args = {'ssusite': 21}
        tc_product_args = {'ssusite': None}

	sb.Rule(f'scan_terminate_from_scan_collision_5_hit_{pos}',
			ssu(**ssu_reactant_args) & tc(**tc_reactant_args) % ssu(**trailing_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) + tc(**tc_product_args) + ssu(**trailing_ssu_product_args) % mrna(**mrna_product_args),
			k)


def scan_terminate_5_hit_elongating(model, ssu, lsu, mrna, pos, k):
	"""Scanning ribosome leaves mRNA at position pos after being hit by a trailing elongating ribosome.
        TC ejected
	"""

	mrna_reactant_args = {f'nt{pos}': 1, f'nt{pos - model.l_ribo}': 2}
	mrna_product_args = {f'nt{pos}': None, f'nt{pos - model.l_ribo}': 2}
        ssu_reactant_args = {'asite': 1, 'hit5': 3, 'hit3': None, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': None, 'hit5': None, 'hit3': None, 'isbi': None, 'tcsite': None}
	trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3, 'isbi': 6}
	trailing_ssu_product_args = {'asite': 2, 'hit3': None, 'isbi': 6}
	trailing_lsu_reactant_args = {'isbi': 6}
	trailing_lsu_product_args = {'isbi': 6}

        tc_reactant_args = {'ssusite': 21}
        tc_product_args = {'ssusite': None}

	sb.Rule(f'scan_terminate_from_elongation_collision_5_hit_{pos}',
			ssu(**ssu_reactant_args) % tc(**tc_reactant_args) % ssu(**trailing_ssu_reactant_args) % lsu(**trailing_lsu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) + tc(**tc_product_args) + ssu(**trailing_ssu_product_args) % lsu(**trailing_lsu_product_args) % mrna(**mrna_product_args),
			k)


def scan_terminate_3_hit_scanning(model, ssu, mrna, pos, k):
	"""Scanning ribosome leaves mRNA at position pos after hitting a leading scanning ribosome.
        TC ejected
	"""

	mrna_reactant_args = {f'nt{pos}': 1, f'nt{pos + model.l_ssu}': 2}
	mrna_product_args = {f'nt{pos}': None, f'nt{pos + model.l_ssu}': 2}
        ssu_reactant_args = {'asite': 1, 'hit5': None, 'hit3': 3, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': None, 'hit5': None, 'hit3': None, 'isbi': None, 'tcsite': None}
	leading_ssu_reactant_args = {'asite': 2, 'hit5': 3, 'isbi': None}
	leading_ssu_product_args = {'asite': 2, 'hit5': None, 'isbi': None}

        tc_reactant_args = {'ssusite': 21}
        tc_product_args = {'ssusite': None}

	# if a scanning ribosome terminates within a footprint from the 5' end, cap is free to bind another PIC
	if pos < model.l_ssu:
		mrna_reactant_args['end5'] = 'blocked'
		mrna_product_args['end5'] = 'free'

	sb.Rule(f'scan_terminate_from_scan_collision_3_hit_{pos}',
			ssu(**ssu_reactant_args) % tc(**tc_reactant_args) & ssu(**leading_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) + tc(**tc_product_args) + ssu(**leading_ssu_product_args) % mrna(**mrna_product_args),
			k)


def scan_terminate_3_hit_elongating(model, ssu, lsu, mrna, pos, k):
	"""Scanning ribosome leaves mRNA at position pos after hitting a leading elongating ribosome.
        TC ejected
	"""

	mrna_reactant_args = {f'nt{pos}': 1, f'nt{pos + model.l_ssu}': 2}
	mrna_product_args = {f'nt{pos}': None, f'nt{pos + model.l_ssu}': 2}
        ssu_reactant_args = {'asite': 1, 'hit5': None, 'hit3': 3, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': None, 'hit5': None, 'hit3': None, 'isbi': None, 'tcsite': None}
	leading_ssu_reactant_args = {'asite': 2, 'hit5': 3, 'isbi': 6}
	leading_ssu_product_args = {'asite': 2, 'hit5': None, 'isbi': 6}
	leading_lsu_reactant_args = {'isbi': 6}
	leading_lsu_product_args = {'isbi': 6}

        tc_reactant_args = {'ssusite': 21}
        tc_product_args = {'ssusite': None}

	# if a scanning ribosome terminates within a footprint from the 5' end, cap is free to bind another PIC
	if pos < model.l_ssu:
		mrna_reactant_args['end5'] = 'blocked'
		mrna_product_args['end5'] = 'free'

	sb.Rule(f'scan_terminate_from_elongation_collision_3_hit_{pos}',
			ssu(**ssu_reactant_args) % tc(**tc_reactant_args) % ssu(**leading_ssu_reactant_args) % lsu(**leading_lsu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) + tc(**tc_product_args) + ssu(**leading_ssu_product_args) % lsu(**leading_lsu_product_args) % mrna(**mrna_product_args),
			k)


def scan_terminate_both_hit_scanning_scanning(model, ssu, mrna, pos, k):
	"""Scanning ribosome leaves mRNA at position pos when hit by leading scanning and trailing scanning ribosomes
        TC ejected
	"""

	mrna_reactant_args = {
		f'nt{pos}': 1, f'nt{pos + model.l_ssu}': 2, f'nt{pos - model.l_ssu}': 3}
	mrna_product_args = {
		f'nt{pos}': None, f'nt{pos + model.l_ssu}': 2, f'nt{pos - model.l_ssu}': 3}
        ssu_reactant_args = {'asite': 1, 'hit5': 4, 'hit3': 5, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': None, 'hit5': None, 'hit3': None, 'isbi': None, 'tcsite': None}
	leading_ssu_reactant_args = {'asite': 2, 'hit5': 5, 'isbi': None}
	leading_ssu_product_args = {'asite': 2, 'hit5': None, 'isbi': None}
	trailing_ssu_reactant_args = {'asite': 3, 'hit3': 4, 'isbi': None}
	trailing_ssu_product_args = {'asite': 3, 'hit3': None, 'isbi': None}

        tc_reactant_args = {'ssusite': 21}
        tc_product_args = {'ssusite': None}

	sb.Rule(f'scan_terminate_from_collision_both_hit_scanning_scanning_{pos}',
			ssu(**ssu_reactant_args) % tc(**tc_reactant_args) % ssu(**leading_ssu_reactant_args) % ssu(**trailing_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) + tc(**tc_product_args) + ssu(**leading_ssu_product_args) % ssu(**trailing_ssu_product_args) % mrna(**mrna_product_args),
			k)


def scan_terminate_both_hit_scanning_elongating(model, ssu, lsu, mrna, pos, k):
	"""Scanning ribosome leaves mRNA at position pos when hit by leading elongating and trailing scanning ribosomes
        TC ejected
	"""

	mrna_reactant_args = {
		f'nt{pos}': 1, f'nt{pos + model.l_ssu}': 2, f'nt{pos - model.l_ssu}': 3}
	mrna_product_args = {
		f'nt{pos}': None, f'nt{pos + model.l_ssu}': 2, f'nt{pos - model.l_ssu}': 3}
        ssu_reactant_args = {'asite': 1, 'hit5': 4, 'hit3': 5, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': None, 'hit5': None, 'hit3': None, 'isbi': None, 'tcsite': None}
	leading_ssu_reactant_args = {'asite': 2, 'hit5': 5, 'isbi': 6}
	leading_ssu_product_args = {'asite': 2, 'hit5': None, 'isbi': 6}
	trailing_ssu_reactant_args = {'asite': 3, 'hit3': 4, 'isbi': None}
	trailing_ssu_product_args = {'asite': 3, 'hit3': None, 'isbi': None}
	leading_lsu_reactant_args = {'isbi': 6}
	leading_lsu_product_args = {'isbi': 6}

        tc_reactant_args = {'ssusite': 21}
        tc_product_args = {'ssusite': None}

	sb.Rule(f'scan_terminate_from_collision_both_hit_scanning_elongating_{pos}',
			ssu(**ssu_reactant_args) % tc(**tc_reactant_args) % ssu(**leading_ssu_reactant_args) % lsu(**leading_lsu_reactant_args) % ssu(**trailing_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) + tc(**tc_reactant_args) + ssu(**leading_ssu_product_args) % lsu(**leading_lsu_product_args) % ssu(**trailing_ssu_product_args) % mrna(**mrna_product_args),
			k)


def scan_terminate_both_hit_elongating_scanning(model, ssu, lsu, mrna, pos, k):
	"""Scanning ribosome leaves mRNA at position pos when hit by leading scanning and trailing elongating ribosomes
        TC ejected
	"""

	mrna_reactant_args = {
		f'nt{pos}': 1, f'nt{pos + model.l_ssu}': 2, f'nt{pos - model.l_ribo}': 3}
	mrna_product_args = {
		f'nt{pos}': None, f'nt{pos + model.l_ssu}': 2, f'nt{pos - model.l_ribo}': 3}
        ssu_reactant_args = {'asite': 1, 'hit5': 4, 'hit3': 5, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': None, 'hit5': None, 'hit3': None, 'isbi': None, 'tcsite': None}
	leading_ssu_reactant_args = {'asite': 2, 'hit5': 5, 'isbi': None}
	leading_ssu_product_args = {'asite': 2, 'hit5': None, 'isbi': None}
	trailing_ssu_reactant_args = {'asite': 3, 'hit3': 4, 'isbi': 6}
	trailing_ssu_product_args = {'asite': 3, 'hit3': None, 'isbi': 6}
	trailing_lsu_reactant_args = {'isbi': 6}
	trailing_lsu_product_args = {'isbi': 6}

        tc_reactant_args = {'ssusite': 21}
        tc_product_args = {'ssusite': None}

	sb.Rule(f'scan_terminate_from_collision_both_hit_elongating_scanning_{pos}',
			ssu(**ssu_reactant_args) % tc(**tc_reactant_args) % ssu(**leading_ssu_reactant_args) % lsu(**trailing_lsu_reactant_args) % ssu(**trailing_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) + tc(**tc_product_args) + ssu(**leading_ssu_product_args) % lsu(**trailing_lsu_product_args) % ssu(**trailing_ssu_product_args) % mrna(**mrna_product_args),
			k)


def scan_terminate_both_hit_elongating_elongating(model, ssu, lsu, mrna, pos, k):
	"""Scanning ribosome leaves mRNA at position pos when hit by leading elongating and trailing elongating ribosomes
        TC ejected
	"""

	mrna_reactant_args = {
		f'nt{pos}': 1, f'nt{pos + model.l_ssu}': 2, f'nt{pos - model.l_ribo}': 3}
	mrna_product_args = {
		f'nt{pos}': None, f'nt{pos + model.l_ssu}': 2, f'nt{pos - model.l_ribo}': 3}
        ssu_reactant_args = {'asite': 1, 'hit5': 4, 'hit3': 5, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': None, 'hit5': None, 'hit3': None, 'isbi': None, 'tcsite': None}
	leading_ssu_reactant_args = {'asite': 2, 'hit5': 5, 'isbi': 8}
	leading_ssu_product_args = {'asite': 2, 'hit5': None, 'isbi': 8}
	trailing_ssu_reactant_args = {'asite': 3, 'hit3': 4, 'isbi': 6}
	trailing_ssu_product_args = {'asite': 3, 'hit3': None, 'isbi': 6}
	leading_lsu_reactant_args = {'isbi': 8}
	leading_lsu_product_args = {'isbi': 8}
	trailing_lsu_reactant_args = {'isbi': 6}
	trailing_lsu_product_args = {'isbi': 6}

        tc_reactant_args = {'ssusite': 21}
        tc_product_args = {'ssusite': None}

	sb.Rule(f'scan_terminate_from_collision_both_hit_elongating_elongating_{pos}',
			ssu(**ssu_reactant_args) % tc(**tc_reactant_args) % ssu(**leading_ssu_reactant_args) % lsu(**leading_lsu_reactant_args) % ssu(**trailing_ssu_reactant_args) % lsu(**trailing_lsu_reactant_args) % mrna(**mrna_reactant_args) >>
			ssu(**ssu_product_args) + tc(**tc_product_args) + ssu(**leading_ssu_product_args) % lsu(**leading_lsu_product_args) % ssu(**trailing_ssu_product_args) % lsu(**trailing_lsu_product_args) % mrna(**mrna_product_args),
			k)
