# For running simulations in a singularity container
container: "../../../bottorff_2022.sif"

# This generates the sim.params.tsv below
include: "choose_simulation_parameters.py"

import pandas as pd
input_params = pd.read_table("sim.params.tsv", index_col=0)

# These rules are run locally
localrules: all

rule all:
  """List of all files we want at the end"""
  input: 
    "analyze_results.md"

rule analyze_data:
  """Analyze simulation results and make figures"""
  input: 
    params = [f'output/model_{n}.params.tsv.gz' for n in range(len(input_params))],
    molecules = [f'output/model_{n}.molecule_type_list.tsv.gz' for n in range(len(input_params))],
    reactions = [f'output/model_{n}.rxn_list.tsv.gz' for n in range(len(input_params))]
  output:
    "analyze_results.md"
  script:
    "analyze_results.Rmd"
  conda: "R"

rule run_simulation:
  """Run simulation for each parameter combination"""
  input:
    "choose_simulation_parameters.py",
  output:
    "output/model_{n}.params.tsv.gz",
    "output/model_{n}.rxn_list.tsv.gz",
    "output/model_{n}.molecule_type_list.tsv.gz"
  conda: "py"
  threads: 1
  shell:
    "python run_simulation.py {wildcards.n}"