"""
Choose parameters for simulation

Vary
- cap binding rate, 1 value 
- uORF2 start codon initiation strength, 2 values
- elongation stall duration, 1 value
- scan abortive termination rate, 2 values
- reinitiation rate, 1 value 
- d_stall length, 5 values

Total of 20 values

- We want to vary reinitiation rate to see if we can fit the strong kozak
control mutant while simultaneously fitting the wt control mutant using the
initiation rate finely varied around a physiological value.
"""

import numpy as np
import pandas as pd
import itertools as it

uorf2_reinitation_fractions = [0.5]

# include each of these params and one of its values in each simulation
and_params = {
    'k_cap_bind': [0.024],
    'k_start_uorf2': [0, 0.5],
    'k_elong_stall': [0.001],
    # we multiply by default k_scan=5 that competes with re-initiation
    'k_terminated_ssu_recycle_uorf2': [5*(1-x) / x for x in uorf2_reinitation_fractions]
}

uorf2_lengths = [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 30, 31, 33]
# exp d_stall list = [66, 69, 72, 75, 78, 87, 96], none are good for ivanov buffering
# add lower d_stall values mirrored across 60 up to 78: 42, 45, 48, 51, 54
# exp uorf2_length list = [23, 24, 25, 26, 27, 30, 33]
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

abort_rates = [0, 2]

abort_params = list()
for rate in abort_rates:
    abort_params.append({
        #        'k_scan_term_5_hit_40s': rate,
        #	'k_scan_term_5_hit_80s': rate,
        'k_scan_term_3_hit_80s': rate,
        'k_scan_term_3_hit_40s': rate,
        'k_scan_term_both_hit_40s_80s': rate,
        'k_scan_term_both_hit_40s_40s': rate,
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
