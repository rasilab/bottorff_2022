"""Program to run simulation with a specific parameter combination

This program

- reads the table of kinetic parameter combinations that we want to simulate
  in this run
- sets simulation time, recording intervals
- gets the specific simulation to run as a number from the command line
- creates a BioNetGen file for that simulation by exporting the PySB model
- runs NFSim simulation using the BioNetGen as input

"""

import sys

import numpy as np
import pandas as pd
from pysb_ul4 import Model
from pysb.export import export
import subprocess as sp
import os

# extract the parameter combination for this simulation
simindex = int(sys.argv[1])
input_params = pd.read_csv('sim.params.tsv', index_col=0, sep='\t')
params_for_this_job = input_params.to_dict(orient='index')[simindex]

# instantiate model with the correct parameters
model = Model(**params_for_this_job)

outdir = './output'
bnglfile = f'{outdir}/model_{simindex}.bngl'
xmlfile = bnglfile.replace('.bngl', '.xml')
gdatfile = bnglfile.replace('.bngl', '.gdat')
paramsfile =  bnglfile.replace('.bngl', '.params.tsv')
moleculesfile = bnglfile.replace('.bngl', '.molecule_type_list.tsv')
rxnlistfile = bnglfile.replace('.bngl', '.rxn_list.tsv')

# write all model parameters to a separate file
with open(paramsfile, 'w') as file:
    file.write('parameter\tvalue\n')
    for param in model.parameters:
        file.write(f'{param.name}\t{param.value}\n')
# compress the params file
sp.run(['gzip', '-f', paramsfile.split('/')[-1]], cwd=outdir)

# write BNGL file
with open(bnglfile, 'w') as file:
    file.write(export(model, 'bngl'))

# convert BNGL file to XML for NFSim input
sp.run(['BNG2.pl', '--xml', '--outdir', outdir, bnglfile])

# parameters for NFsim
equilibrium_time = 0  # seconds
tstop = str(1000000)  # seconds
maxcputime = str(2000 * 60)  # seconds
osteps = str(10)  # number of time samples
seed = str(111)  # random number initial seed
gml = str(1000000)  # max num of mol allowed in simulation
utl = '3'  # max number of bonds to traverse during simulation
network = '-connect'  # whether to infer reaction network connectivity

# print NFSim command
nfsim_command = [
    'NFsim', '-xml', xmlfile, '-sim', tstop, '-oSteps', osteps,
    '-seed', seed, '-o', gdatfile, 
    '-utl', utl,
    '-gml', gml, '-maxcputime', maxcputime,
    network, 
    '-printmoltypes', '-printrxncounts'
    #     '-trackconnected'
#have the trackconnected hashtagged out when running on cluster
]
print(' '.join(nfsim_command))

# simlate with NFSim
sp.run(nfsim_command, stdout=sp.DEVNULL)

# remove the files that are too big or are not needed for analysis
# comment these lines out for troubleshooting
os.remove(gdatfile)
os.remove(bnglfile)
os.remove(xmlfile)

# compress the molecule and rxn list file
sp.run(['gzip', '-f', moleculesfile.split('/')[-1]], cwd=outdir)
sp.run(['gzip', '-f', rxnlistfile.split('/')[-1]], cwd=outdir)