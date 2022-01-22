import pysb as sb
import copy


def bind_cap_pic(tc, ssu, mrna, pos, k):
    """The PIC binds to the mRNA position pos at rate k
        and blocks subsequent PICs from binding by blocking the 5' end.
    """

    sb.Rule(f'bind_cap_pic_{pos}',
            ssu(asite=None, tcsite=2) % tc(ssusite=2) +
            mrna(**{f'nt{pos}': None, 'end5': 'free'}) >>
            ssu(asite=1, tcsite=2) % tc(ssusite=2) % mrna(
                **{f'nt{pos}': 1, 'end5': 'blocked'}),
            k, total_rate=True)


def bind_tc_free_ssu(tc, ssu, k):
    """The ternary complex binds to an ssu not bound by a large subunit.
    This is required for cap binding.
    The tcsite and isbi cannot be occupied at the same time (ternary complex
    leaves before large subunit joins), we do not put this as a constraint
    in the model, but implement this constraint in our rule specification.
    """

    sb.Rule('tc_free_ssu_binding',
            ssu(tcsite=None, isbi=None) +
            tc(ssusite=None) >> ssu(tcsite=1, isbi=None) % tc(ssusite=1),
            k, total_rate=False)


def scan(model, tc, ssu, lsu, mrna, pos, k):
    """The PIC scans from mRNA position pos to pos + 1 at rate k.
    This can occur only if it not blocked by a leading scanning or elongating ribosome.
    """

    mrna_reactant_args = {f'nt{pos}': 1, f'nt{pos + 1}': None}
    mrna_product_args = {f'nt{pos}': None, f'nt{pos + 1}': 1}

    ssu_reactant_args = {'asite': 1, 'hit5': None,
                            'hit3': None, 'isbi': None, 'terminating': None}
    ssu_product_args = {'asite': 1, 'hit5': None,
                        'hit3': None, 'isbi': None, 'terminating': 'no'}

    # PICs can scan only if there is no scanning or elongating ribosome in front.
    # applies only if another ribosome can fit in the 3' side.
    if (pos < model.l_mrna - model.l_ssu and model.l_ssu > 1):
        mrna_reactant_args[f'nt{pos + model.l_ssu}'] = None
        mrna_product_args[f'nt{pos + model.l_ssu}'] = None

    # if ribosome scans beyond a footprint from 5' end, cap is free to bind another PIC
    if pos == model.l_ssu - 1:
        mrna_reactant_args['end5'] = 'blocked'
        mrna_product_args['end5'] = 'free'

    sb.Rule(f'scan_{pos}',
            ssu(**ssu_reactant_args) % mrna(**mrna_reactant_args) >> 
            ssu(**ssu_product_args) % mrna(**mrna_product_args),
            k)

    # create temporary copy of mrna_reactant and mrna_product args for different conditions
    mrna_reactant_temp = copy.deepcopy(mrna_reactant_args)
    mrna_product_temp = copy.deepcopy(mrna_product_args)

    # scan out of a collision with a trailing scanning ribosome
    mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
    mrna_product_args = copy.deepcopy(mrna_product_temp)
    if pos > model.l_ssu - 1:
        mrna_reactant_args[f'nt{pos - model.l_ssu}'] = 2
        mrna_product_args[f'nt{pos - model.l_ssu}'] = 2
        ssu_reactant_args['hit5'] = 3
        ssu_product_args['hit5'] = None
        trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3, 'isbi': None}
        trailing_ssu_product_args = {
            'asite': 2, 'hit3': None, 'isbi': None}
        sb.Rule(f'scan_from_scan_collision_{pos}',
                ssu(**ssu_reactant_args) % ssu(**trailing_ssu_reactant_args) % 
                mrna(**mrna_reactant_args) >>
                ssu(**ssu_product_args) % ssu(**trailing_ssu_product_args) % 
                mrna(**mrna_product_args),
                k)

    # scan out of a collision with a trailing elongating ribosome
    mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
    mrna_product_args = copy.deepcopy(mrna_product_temp)
    if pos > model.l_ribo - 1:
        mrna_reactant_args[f'nt{pos - model.l_ribo}'] = 2
        mrna_product_args[f'nt{pos - model.l_ribo}'] = 2
        ssu_reactant_args['hit5'] = 3
        ssu_product_args['hit5'] = None
        trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3, 'isbi': 6}
        trailing_ssu_product_args = {'asite': 2, 'hit3': None, 'isbi': 6}
        trailing_lsu_reactant_args = {'isbi': 6}
        trailing_lsu_product_args = {'isbi': 6}
        sb.Rule(f'scan_from_elongation_collision_{pos}',
                ssu(**ssu_reactant_args) % ssu(**trailing_ssu_reactant_args) % 
                lsu(**trailing_lsu_reactant_args) % mrna(**mrna_reactant_args) >>
                ssu(**ssu_product_args) % ssu(**trailing_ssu_product_args) % 
                lsu(**trailing_lsu_product_args) % mrna(**mrna_product_args),
                k)

def backwards_scan(model, tc, ssu, lsu, mrna, pos, k):
    """The PIC scans from mRNA position pos to pos - 1 at rate k.
    This can occur only if it not blocked by a trailing scanning or elongating ribosome.
    """

    mrna_reactant_args = {f'nt{pos}': 1, f'nt{pos - 1}': None}
    mrna_product_args = {f'nt{pos}': None, f'nt{pos - 1}': 1}

    ssu_reactant_args = {'asite': 1, 'hit5': None,
                            'hit3': None, 'isbi': None, 'terminating': None}
    ssu_product_args = {'asite': 1, 'hit5': None,
                        'hit3': None, 'isbi': None, 'terminating': 'no'}

    # PICs can backwards scan only if there is no scanning or elongating ribosome in back.
    # applies only if another ribosome can fit in the 5' side.
    if ((pos > model.l_ssu - 1) and (model.l_ssu > 1)):
        mrna_reactant_args[f'nt{pos - model.l_ssu}'] = None
        mrna_product_args[f'nt{pos - model.l_ssu}'] = None
    # if ribosome backwards scans into footprint from 5' end, cap is no longer free to bind another PIC
    if pos == model.l_ssu:
        mrna_reactant_args['end5'] = 'free'
        mrna_product_args['end5'] = 'blocked'

    sb.Rule(f'backwards_scan_{pos}',
            ssu(**ssu_reactant_args) % mrna(**mrna_reactant_args) >> 
            ssu(**ssu_product_args) % mrna(**mrna_product_args),
            k)

    # create temporary copy of mrna_reactant and mrna_product args for different conditions
    mrna_reactant_temp = copy.deepcopy(mrna_reactant_args)
    mrna_product_temp = copy.deepcopy(mrna_product_args)

    # backwards scan out of a collision with a leading scanning ribosome
    mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
    mrna_product_args = copy.deepcopy(mrna_product_temp)
    if pos < model.l_mrna - model.l_ssu:
        mrna_reactant_args[f'nt{pos + model.l_ssu}'] = 2
        mrna_product_args[f'nt{pos + model.l_ssu}'] = 2
        ssu_reactant_args['hit3'] = 3
        ssu_product_args['hit3'] = None
        leading_ssu_reactant_args = {'asite': 2, 'hit5': 3, 'isbi': None}
        leading_ssu_product_args = {
            'asite': 2, 'hit5': None, 'isbi': None}
        sb.Rule(f'backwards_scan_from_scan_collision_{pos}',
                ssu(**ssu_reactant_args) % ssu(**leading_ssu_reactant_args) % 
                mrna(**mrna_reactant_args) >>
                ssu(**ssu_product_args) % ssu(**leading_ssu_product_args) % 
                mrna(**mrna_product_args),
                k)

    # backwards scan out of a collision with a leading elongating ribosome
    mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
    mrna_product_args = copy.deepcopy(mrna_product_temp)
    if pos < model.l_mrna - model.l_ribo:
        mrna_reactant_args[f'nt{pos + model.l_ribo}'] = 2
        mrna_product_args[f'nt{pos + model.l_ribo}'] = 2
        ssu_reactant_args['hit3'] = 3
        ssu_product_args['hit3'] = None
        leading_ssu_reactant_args = {'asite': 2, 'hit5': 3, 'isbi': 6}
        leading_ssu_product_args = {'asite': 2, 'hit5': None, 'isbi': 6}
        leading_lsu_reactant_args = {'isbi': 6}
        leading_lsu_product_args = {'isbi': 6}
        sb.Rule(f'backwards_scan_from_elongation_collision_{pos}',
                ssu(**ssu_reactant_args) % ssu(**leading_ssu_reactant_args) % 
                lsu(**leading_lsu_reactant_args) % mrna(**mrna_reactant_args) >>
                ssu(**ssu_product_args) % ssu(**leading_ssu_product_args) % 
                lsu(**leading_lsu_product_args) % mrna(**mrna_product_args),
                k)

def scan_to_elongate(model, tc, ssu, lsu, mrna, pos, k, newpos):
    """Convert scanning ribosomes at pos to elongating ribosomes at newpos.
    The relocation of the A-site requires that that are no leading or following 
    ssu / 80S that block this relocation.
    If the 80S is larger than PIC, then there needs to be enough space for an 
    80S footprint.
    """

    ssu_reactant_args = {'asite': 1, 'hit5': None,
                            'hit3': None, 'isbi': None, 'tcsite': 21}
    ssu_product_args = {'asite': 1, 'hit5': None,
                        'hit3': None, 'isbi': 8, 'tcsite': None}
    lsu_reactant_args = {'isbi': None}
    lsu_product_args = {'isbi': 8}
    tc_reactant_args = {'ssusite': 21}
    tc_product_args = {'ssusite': None}

    if pos != newpos:
        mrna_reactant_args = {f'nt{pos}': 1, f'nt{newpos}': None}
        mrna_product_args = {f'nt{pos}': None, f'nt{newpos}': 1}
        # account for relocation to the 5' side.
        if newpos < pos:
            for loc in range(pos, newpos, -1):
                if loc-model.l_ribo >= 0:
                    mrna_reactant_args[f'nt{loc-model.l_ribo}'] = None
                    mrna_product_args[f'nt{loc-model.l_ribo}'] = None
                if loc-model.l_ssu >= 0:
                    mrna_reactant_args[f'nt{loc-model.l_ssu}'] = None
                    mrna_product_args[f'nt{loc-model.l_ssu}'] = None
        # account for relocation to the 3' side
        if newpos > pos:
            for loc in range(pos, newpos):
                if loc+model.l_ribo < model.l_mrna:
                    mrna_reactant_args[f'nt{loc+model.l_ribo}'] = None
                    mrna_product_args[f'nt{loc+model.l_ribo}'] = None
                if loc+model.l_ssu < model.l_mrna:
                    mrna_reactant_args[f'nt{loc+model.l_ssu}'] = None
                    mrna_product_args[f'nt{loc+model.l_ssu}'] = None
    else:
        mrna_reactant_args = {f'nt{pos}': 1}
        mrna_product_args = {f'nt{pos}': 1}

    # account for change in ribosome footprint
    if model.l_ribo > model.l_ssu:
        for loc in range(pos+model.l_ssu, pos+model.l_ribo):
            if loc < model.l_mrna:
                mrna_reactant_args[f'nt{loc}'] = None
                mrna_product_args[f'nt{loc}'] = None

    sb.Rule(f'scan_to_elongate_{pos}',
            ssu(**ssu_reactant_args) % tc(**tc_reactant_args) % 
            mrna(**mrna_reactant_args) + lsu(**lsu_reactant_args) >>
            ssu(**ssu_product_args) % mrna(**mrna_product_args) % 
            lsu(**lsu_product_args) + tc(**tc_product_args),
            k, total_rate=True)

    # create temporary copy of mrna_reactant and mrna_product args for different conditions
    mrna_reactant_temp = copy.deepcopy(mrna_reactant_args)
    mrna_product_temp = copy.deepcopy(mrna_product_args)

    # come out of a collision with a trailing scanning ribosome
    if ((pos > model.l_ssu - 1) and (newpos >= pos)):
        mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
        mrna_product_args = copy.deepcopy(mrna_product_temp)
        mrna_reactant_args[f'nt{pos - model.l_ssu}'] = 2
        mrna_product_args[f'nt{pos - model.l_ssu}'] = 2
        ssu_reactant_args = {'asite': 1, 'hit5': 3,
                                'hit3': None, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': 1, 'hit5': None,
                            'hit3': None, 'isbi': 8, 'tcsite': None}
        trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3, 'isbi': None}
        trailing_ssu_product_args = {
            'asite': 2, 'hit3': None, 'isbi': None}
        sb.Rule(f'scan_to_elongate_from_trailing_scan_collision_{pos}',
                lsu(**lsu_reactant_args) + ssu(**ssu_reactant_args) % 
                tc(**tc_reactant_args) % ssu(**trailing_ssu_reactant_args) % 
                mrna(**mrna_reactant_args) >>
                lsu(**lsu_product_args) % ssu(**ssu_product_args) % 
                ssu(**trailing_ssu_product_args) % mrna(**mrna_product_args) + 
                tc(**tc_product_args),
                k, total_rate=True)

    # come out of a collision with a trailing elongating ribosome
    if ((pos > model.l_ribo - 1) and (newpos >= pos)):
        mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
        mrna_product_args = copy.deepcopy(mrna_product_temp)
        mrna_reactant_args[f'nt{pos - model.l_ribo}'] = 2
        mrna_product_args[f'nt{pos - model.l_ribo}'] = 2
        ssu_reactant_args = {'asite': 1, 'hit5': 3,
                                'hit3': None, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': 1, 'hit5': None,
                            'hit3': None, 'isbi': 8, 'tcsite': None}
        trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3, 'isbi': 6}
        trailing_ssu_product_args = {'asite': 2, 'hit3': None, 'isbi': 6}
        trailing_lsu_reactant_args = {'isbi': 6}
        trailing_lsu_product_args = {'isbi': 6}
        sb.Rule(f'scan_to_elongate_from_trailing_elongation_collision_{pos}',
                lsu(**lsu_reactant_args) + ssu(**ssu_reactant_args) % 
                tc(**tc_reactant_args) % ssu(**trailing_ssu_reactant_args) % 
                lsu(**trailing_lsu_reactant_args) % mrna(**mrna_reactant_args) >>
                lsu(**lsu_product_args) % ssu(**ssu_product_args) % 
                ssu(**trailing_ssu_product_args) % 
                lsu(**trailing_lsu_product_args) % 
                mrna(**mrna_product_args) + tc(**tc_product_args),
                k, total_rate=True)

    # come out of a collision with a leading scanning or elongating ribosome
    if ((pos < model.l_mrna - model.l_ssu - 1) and (newpos <= pos)):
        mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
        mrna_product_args = copy.deepcopy(mrna_product_temp)
        mrna_reactant_args[f'nt{pos + model.l_ssu}'] = 2
        mrna_product_args[f'nt{pos + model.l_ssu}'] = 2
        ssu_reactant_args = {'asite': 1, 'hit5': None,
                                'hit3': 3, 'isbi': None, 'tcsite': 21}
        ssu_product_args = {'asite': 1, 'hit5': None,
                            'hit3': None, 'isbi': 8, 'tcsite': None}
        leading_ssu_reactant_args = {'asite': 2, 'hit5': 3}
        leading_ssu_product_args = {'asite': 2, 'hit5': None}
        sb.Rule(f'scan_to_elongate_from_leading_collision_{pos}',
                lsu(**lsu_reactant_args) + ssu(**ssu_reactant_args) % 
                tc(**tc_reactant_args) % ssu(**leading_ssu_reactant_args) 
                % mrna(**mrna_reactant_args) >>
                lsu(**lsu_product_args) % ssu(**ssu_product_args) % ssu(
                    **leading_ssu_product_args) % mrna(**mrna_product_args) +
                     tc(**tc_product_args),
                k, total_rate=True)
