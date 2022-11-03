base_folder=$(pwd)
experiments_folder=base_folder/experiments
computational_folder=base_folder/computational
simulations_folder=computational_folder/simulation_runs

conda init bash

# Comment out below commands if not using Singularity
grabnode # for fred hutch only, get max 36 nodes, max 720G memory, for **1** day, with no GPU
echo "Loading modules"
module load Singualarity
conda activate snakemake
echo "Pulling Singularity container from Github"
singularity pull docker://ghcr.io/rasilab/bottorff_2022

# Experiments
echo "Performing experimental analyses"

# figures 2C & S1B
cd experiments_folder/platform_controls/scripts
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@
cp ../tables/nluc_fluc_control_mutants.csv simulations_folder/80s_hit_model_fitting/tables/
cp ../tables/nluc_fluc_control_mutants.csv simulations_folder/queuing_dissociation_models_fitting/tables/
cp ../tables/nluc_fluc_control_mutants_not_normalized.csv experiments_folder/drug_buffering/tables/

# figure 5A
cd experiments_folder/stem_loop_buffering/scripts
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figure 5B
cd experiments_folder/drug_buffering/scripts
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figure 5C
cd experiments_folder/synthetic_uorf_buffering/scripts
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figure 6B
cd experiments_folder/d_stall_repressiveness/scripts
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figure 6C
cd experiments_folder/d_stall_buffering/scripts
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figure 7
cd experiments_folder/human_uorfs/scripts
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figure S1A
cd experiments_folder/supplemental_platform_controls/scripts
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figure S4
cd experiments_folder/supplemental_d_stall_repressiveness/scripts
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# computational
echo "Performing computational analyses"

# figure 2D
cd simulations_folder/80s_hit_model_fitting
mkdir output
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@
cd simulations_folder/queuing_dissociation_models_fitting
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figures 4A, 4C, 4D, S2C, S2E, S2F
cd simulations_folder/constitutive_queuing_dissociation_models_buffering
mkdir output
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figures 4B, S2A, S2B, S3B
cd simulations_folder/80s_hit_model_buffering
mkdir output
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figures 4E, S3A
cd simulations_folder/regulated_reinitiation_model_buffering
mkdir output
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figure 6A
cd simulations_folder/backward_scanning_d_stall_periodicity
mkdir output
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figure S2D
cd simulations_folder/backward_scanning_buffering
mkdir output
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@

# figure S5 (ribosome density over uORFs with conserved stalling peptides)
cd computational_folder/uorf_ribosome_density/scripts
sh submit_cluster.sh "--snakefile" analyze_results.smk "--forceall" $@