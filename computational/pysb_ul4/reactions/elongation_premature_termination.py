import pysb as sb


def elong_preterm_no_hit(model, ssu, lsu, mrna, pos, k):
    """An 80S on mRNA prematurely aborts translation. We consider only elongating ribosomes
        that are not hit from 5' or 3' side
        """
    mrna_reactant_args = {f'nt{pos}': 1}
    mrna_product_args = {f'nt{pos}': None}

    ssu_reactant_args = {'asite': 1, 'isbi': 8,
                         'hit5': None, 'hit3': None, 'tcsite': None}
    ssu_product_args = {'asite': None, 'isbi': None,
                        'hit5': None, 'hit3': None, 'tcsite': None}

    lsu_reactant_args = {'isbi': 8}
    lsu_product_args = {'isbi': None}

    sb.Rule(f'elong_preterm_no_hit_{pos}',
            ssu(**ssu_reactant_args) % lsu(**lsu_reactant_args) % mrna(**mrna_reactant_args) >>
            lsu(**lsu_product_args) + ssu(**ssu_product_args) +
            mrna(**mrna_product_args),
            k)
