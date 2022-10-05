"""Run simulation with default values if the file is run as a script.

    Will create output files in the current working directory
    """

import argparse
import sys
import subprocess as sp
from pysb_ul4 import Model
from pysb.export import export

parser = argparse.ArgumentParser(description='Run simulation.')
parser.add_argument('--bng2', type=str, metavar='BNG2.pl',
                    help='Path to BioNetGen BNG2.pl script (default: BNG2.pl)',
                    default='BNG2.pl')
parser.add_argument('--nfsim', type=str, metavar='NFsim',
                    help='Path to NFsim executable (default: NFsim)',
                    default='NFsim')
args = parser.parse_args()

equilibrium_time = 0  # seconds
tstop = str(10000)  # seconds
maxcputime = str(100 * 60)  # seconds
osteps = str(10)  # number of samples
seed = str(111)  # random number initial seed
gml = str(1000000)  # max num of mol allowed in simulation
utl = '3'  # max number of bonds to traverse during simulation
network = '-connect'  # whether to infer reaction network connectivity

# instantiate the model class with default parameter values
model = Model()

outdir = '.'
bnglfile = f'{outdir}/ul4.bngl'
xmlfile = bnglfile.replace('.bngl', '.xml')
gdatfile = bnglfile.replace('.bngl', '.gdat')
rxnfile = bnglfile.replace('.bngl', '.rxns.tsv')

# write BNGL file
with open(bnglfile, 'w') as file:
    file.write(export(model, 'bngl'))

# convert BNGL file to XML for NFSim input
sp.run([args.bng2, '--xml', '--outdir', outdir, bnglfile])

# simlate with NFSim
# print NFSim command
nfsim_command = [
    args.nfsim, '-xml', xmlfile, '-sim', tstop, '-oSteps', osteps,
    '-seed', seed, '-o', gdatfile, '-rxnlog', rxnfile,
    '-utl', utl,
    '-gml', gml, '-maxcputime', maxcputime,
    network
]
print(" ".join(nfsim_command))

# simlate with NFSim
sp.run(nfsim_command)