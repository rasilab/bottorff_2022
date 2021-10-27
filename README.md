#+TITLE: Translational buffering by ribosome stalling in upstream open reading frames

Paper citation

Paper link

[[http://rasilab.fredhutch.org/]]

This repository contains raw experimental data, code, and instructions for:
 - running simulations
 - generating figures in the manuscript

** Modeling

*** Default run

To run the simulations, install our lab's customized versions of:
- [[https://www.ncbi.nlm.nih.gov/pubmed/23423320][PySB]]: https://github.com/rasilab/PySB
- [[https://www.ncbi.nlm.nih.gov/pubmed/27402907][BioNetGen]]: https://github.com/rasilab/BioNetGen
- [[https://www.ncbi.nlm.nih.gov/pubmed/21186362][NFsim]]: https://github.com/rasilab/NFsim

The instructions for installing the above software are provided in the respective links.

Our kinetic model for quality control during eukaryotic translation is defined in [[file:]]. 
This model is defined using the [[http://pysb.org/][PySB]] syntax.
To simulate this model with its default parameters, run:
#+BEGIN_SRC sh :exports code
cd modeling
python tasep.py
#+END_SRC

The above run displays the following output:
#+BEGIN_SRC

#+END_SRC

CPU times will be a bit different depending on the machine.

At the end of the run, =files= files should be present in the [[file:modeling/]] folder.

*** Parameter sweep

Simulations with systematic variation of parameters are run from the 9 sub-directories in [[file:modeling/]].
Each of these sub-directories contains a [[https://snakemake.readthedocs.io/en/stable/][Snakemake]] workflow that chooses the parameters and runs the simulations.
Below, we describe this workflow using a specific example in the [[file:modeling/simulation_runs/]] sub-directory that generated Fig. 3A in our paper.
All other sub-directories contain a very similar workflow.

For the set of x simulations in [[file:modeling/simulation_runs/]], y param is systematically varied.
The parameters that are varied from their default values are chosen in [[file:modeling/simulation_runs/choose_simulation_parameters.py]] and written as a tab-separated file [[file:modeling/simulation_runs/sim.params.tsv]] in the same directory.
The script [[file:modeling/simulation_runs/run_simulation.py]] runs the simulation with a single parameter set. 
This parameter set is decided by the single argument to this script which specifies the row number in [[file:modeling/simulation_runs/sim.params.tsv]].

Simulations are often run on a cluster using the cluster configuration [[file:modeling/simulation_runs/csat_model_vary_num_stalls/cluster.yaml]].

To invoke the above workflow, run:
#+BEGIN_SRC sh :exports code
cd modeling/simulation_runs/
# check what will be run using a dry run
snakemake -np
# use a SLURM cluster for running simulations
sh submit_cluster.sh > submit.log 2> submit.log &
# uncomment line below to run everything locally; can take a very long time!!
# snakemake
#+END_SRC

** Source data for figures

The RMarkdown scripts can be knitted to generate the figures by:

#+BEGIN_SRC sh :exports code
cd analysis/flow
for file in *.Rmd; do R -e "rmarkdown::render('$file')"; done
#+END_SRC