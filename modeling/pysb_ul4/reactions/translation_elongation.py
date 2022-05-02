import pysb as sb
import copy


def elongate(model, ssu, lsu, mrna, pos, k):
    """The 80S moves from mRNA position pos to pos + 3 at rate k.
        This can occur only if it not blocked by a leading scanning or elongating ribosome.
        """

    mrna_reactant_args = {f'nt{pos}': 1, f'nt{pos + 3}': None}
    mrna_product_args = {f'nt{pos}': None, f'nt{pos + 3}': 1}

    ssu_reactant_args = {'asite': 1, 'hit5': None, 'hit3': None, 'isbi': 8}
    ssu_product_args = {'asite': 1, 'hit5': None, 'hit3': None, 'isbi': 8}

    lsu_reactant_args = {'isbi': 8}
    lsu_product_args = {'isbi': 8}

    # 80S can elongate only if there is no scanning or elongating ribosome in front.
    # applies only if another ribosome can fit in the 3' side.
    # The  -2 accounts for the 3 different frames
    if (pos < model.l_mrna - model.l_ribo - 2 and model.l_ribo > 1):
        # check that all 3 frames are not occupied by another elongating or scanning ribosome
        for frame in range(3):
            mrna_reactant_args[f'nt{pos + model.l_ribo + frame}'] = None
            mrna_product_args[f'nt{pos + model.l_ribo + frame}'] = None

    # if ribosome elongates beyond a footprint from 5' end, cap is free to bind another PIC.
    # need to consider all 3 frames since the ribosome elongates in steps of 3 nt.
    if pos in list(range(model.l_ssu - 3, model.l_ssu)):
        mrna_reactant_args['end5'] = 'blocked'
        mrna_product_args['end5'] = 'free'

    sb.Rule(f'elongate_{pos}',
            ssu(**ssu_reactant_args) % lsu(**lsu_reactant_args) % mrna(**mrna_reactant_args) >>
            ssu(**ssu_product_args) % lsu(**
                                            lsu_product_args) % mrna(**mrna_product_args),
            k)

    # create temporary copy of mrna_reactant and mrna_product args for different conditions
    mrna_reactant_temp = copy.deepcopy(mrna_reactant_args)
    mrna_product_temp = copy.deepcopy(mrna_product_args)

    # elongate out of a collision with a trailing scanning ribosome
    mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
    mrna_product_args = copy.deepcopy(mrna_product_temp)
    if pos > model.l_ssu - 1:
        mrna_reactant_args[f'nt{pos - model.l_ssu}'] = 2
        mrna_product_args[f'nt{pos - model.l_ssu}'] = 2
        ssu_reactant_args = {'asite': 1,
                                'hit5': 3, 'hit3': None, 'isbi': 8}
        ssu_product_args = {'asite': 1,
                            'hit5': None, 'hit3': None, 'isbi': 8}
        trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3, 'isbi': None}
        trailing_ssu_product_args = {
            'asite': 2, 'hit3': None, 'isbi': None}
        sb.Rule(f'elongate_from_scan_collision_{pos}',
                ssu(**ssu_reactant_args) % lsu(**lsu_reactant_args) % ssu(**trailing_ssu_reactant_args) % mrna(**mrna_reactant_args) >>
                ssu(**ssu_product_args) % lsu(**lsu_reactant_args) % ssu(**
                                                                            trailing_ssu_product_args) % mrna(**mrna_product_args),
                k)

    # elongate out of a collision with a trailing elongating ribosome
    mrna_reactant_args = copy.deepcopy(mrna_reactant_temp)
    mrna_product_args = copy.deepcopy(mrna_product_temp)
    if pos > model.l_ribo - 1:
        mrna_reactant_args[f'nt{pos - model.l_ribo}'] = 2
        mrna_product_args[f'nt{pos - model.l_ribo}'] = 2
        ssu_reactant_args = {'asite': 1,
                                'hit5': 3, 'hit3': None, 'isbi': 8}
        ssu_product_args = {'asite': 1,
                            'hit5': None, 'hit3': None, 'isbi': 8}
        trailing_ssu_reactant_args = {'asite': 2, 'hit3': 3, 'isbi': 6}
        trailing_ssu_product_args = {'asite': 2, 'hit3': None, 'isbi': 6}
        trailing_lsu_reactant_args = {'isbi': 6}
        trailing_lsu_product_args = {'isbi': 6}
        sb.Rule(f'elongate_from_elongation_collision_{pos}',
                ssu(**ssu_reactant_args) % lsu(**lsu_reactant_args) % 
                ssu(**trailing_ssu_reactant_args) % 
                lsu(**trailing_lsu_reactant_args) % 
                mrna(**mrna_reactant_args) >>
                ssu(**ssu_product_args) % lsu(**lsu_reactant_args) % 
                ssu(**trailing_ssu_product_args) % 
                lsu(**trailing_lsu_product_args) % mrna(**mrna_product_args),
                k)
