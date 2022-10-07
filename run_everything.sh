#! /bin/bash

# Script for running all simulations and analyses

echo $@

if [ X$1 = X"--use-singularity" ]
then
    SINGULARITY_ARGS="--use-singularity"
else
    SINGULARITY_ARGS=""
fi

if [ X$2 = X"--use-cluster" ]
then
    CLUSTER_ARGS="-p --jobs 999 --cluster-config ../../../.snakemake_profile/cluster.yaml --restart-times 2 --nolock --cluster"
    SLURM_COMMAND="sbatch -n {cluster.n}  -t {cluster.time}"
else
    CLUSTER_ARGS="-p --cores=8"
    SLURM_COMMAND=""
fi

# Experiments

# figures 2C & S1B
cd experiments/platform_controls/scripts
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS
cp ../tables/nluc_fluc_control_mutants.csv ../../../computational/simulation_runs/80s_hit_model_fitting/tables/
cp ../tables/nluc_fluc_control_mutants.csv ../../../computational/simulation_runs/queuing_dissociation_models_fitting/tables/
cp ../tables/nluc_fluc_control_mutants_not_normalized.csv ../../drug_buffering/tables/

# figure 5A
cd ../../stem_loop_buffering/scripts
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figure 5B
cd ../../drug_buffering/scripts
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figure 5C
cd ../../synthetic_uorf_buffering/scripts
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figure 6B
cd ../../d_stall_repressiveness/scripts
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figure 6C
cd ../../d_stall_buffering/scripts
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figure 7
cd ../../human_uorfs/scripts
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figure S1A
cd ../../supplemental_platform_controls/scripts
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figure S4
cd ../../supplemental_d_stall_repressiveness/scripts
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# computational

# figure 2D
cd ../../../computational/simulation_runs/80s_hit_model_fitting
mkdir output
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS
cd ../queuing_dissociation_models_fitting
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figures 4A, 4C, 4D, S2C, S2E, S2F
cd ../constitutive_queuing_dissociation_models_buffering
mkdir output
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figures 4B, S2A, S2B, S3B
cd ../80s_hit_model_buffering
mkdir output
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figures 4E, S3A
cd ../regulated_reinitiation_model_buffering
mkdir output
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figure 6A
cd ../backward_scanning_d_stall_periodicity
mkdir output
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figure S2D
cd ../backward_scanning_buffering
mkdir output
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS

# figure S5 (ribosome density over uORFs with conserved stalling peptides)
cd ../../uorf_ribosome_density/scripts
snakemake $CLUSTER_ARGS $SLURM_COMMAND $SINGULARITY_ARGS