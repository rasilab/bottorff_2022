"""
Choose parameters for simulation

Vary
- uORF2 start codon initiation strength, 3 values
- uORF2 continued scanning rate, 2 values
- uORF3 start codon initiation strength, 3 values
- uORF3 continued scanning rate, 2 values
- number of ternary complexes, 11 values 

Total of 396 values

"""

import numpy as np
import pandas as pd
import itertools as it

# include each of these params and one of its values in each simulation
and_params = {
    'k_cap_bind': [0.125],
    'k_start_uorf2': [0, 4/3, 200],
    'k_terminated_ssu_recycle_uorf2': [2/99, 495],
    'k_start_uorf3': [0, 4/3, 200],
    'k_terminated_ssu_recycle_uorf3': [2/99, 495],
    'n_tc_0': 2**np.arange(10, -1, -1),
    }

uorf2_lengths = [22]
uorf2_starts = [25]
length_params = list()
for l, n in it.product(uorf2_lengths, uorf2_starts):
    # n = 25 nt is the default value for the gp48 mRNA
    uorf2_start = n
    uorf2_stop = uorf2_start + 3 * l
    x_stall = uorf2_start + 3 * (l-1)
    # the distance between uorf2 and uorf3, main orf is same as gp48
    # the length of the main orf does not matter
    uorf3_start = uorf2_stop + 6
    uorf3_stop = uorf3_start + 9
    orf_start = uorf2_stop + 141
    orf_stop = orf_start + 45
    # mrna is just longer than main ORF
    l_mrna = orf_stop + 3

    length_params.append({
        'uorf2_start': uorf2_start,
        'uorf2_stop': uorf2_stop,
        'uorf3_start': uorf3_start,
        'uorf3_stop': uorf3_stop,
        'orf_start':  orf_start,
        'orf_stop': orf_stop,
        'l_mrna': l_mrna,
        'x_stall': x_stall
    })

abort_rates = [0]

abort_params = list()
for rate in abort_rates:
    abort_params.append({
        #        'k_scan_term_5_hit_40s': rate,
        	'k_scan_term_5_hit_80s': rate,
        #'k_scan_term_3_hit_80s': rate,
        #'k_scan_term_3_hit_40s': rate,
        #'k_scan_term_both_hit_40s_80s': rate,
        #'k_scan_term_both_hit_40s_40s': rate,
        'k_scan_term_both_hit_80s_40s': rate,
        'k_scan_term_both_hit_80s_80s': rate,
    })


# create a list of all parameter combinations from above dict
# there will be as many list elements as the product of all list lengths above
and_params = [list(x) for x in it.product(*[[(p, v)
                                             for v in and_params[p]]
                                            for p in and_params])]

# convert each param combination from dict to list of tuples
length_params = [list(x.items()) for x in length_params]
abort_params = [list(x.items()) for x in abort_params]

# combine the 'and' parameters and parameter combinations from above
simcount = 0
temp = dict()
for params in it.product(and_params, length_params, abort_params):
    temp[simcount] = dict(it.chain.from_iterable(params))
    simcount += 1

# convert to pandas dataframe
input_params = pd.DataFrame.from_dict(temp, orient='index')

# sort  the paramters by these parameter combinations
input_params = input_params.sort_values(
    by=['k_cap_bind', 'l_mrna']).reset_index(drop=True)
input_params.index.name = 'sim_id'

input_params.to_csv('sim.params.tsv', sep='\t')  # write to tab-delimited file
input_params.info()  # display the table of input parameters