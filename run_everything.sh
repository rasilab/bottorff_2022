# Script for running all simulations and analyses

echo $@

if [ $1 = "--use-singularity" ]
then
    SINGULARITY_ARGS="--use-singularity"
else
    SINGULARITY_ARGS=""
fi

if [ $2 = "--use-cluster" ]
then
    CLUSTER_ARGS="-p --jobs 999 --cluster-config ../../../.snakemake_profile/cluster.yaml --restart-times 2 --nolock --cluster"
    SLURM_COMMAND="sbatch -n {cluster.n}  -t {cluster.time}"
else
    CLUSTER_ARGS="-p --cores=8"
    SLURM_COMMAND=""
fi

# Experiments

# figure 2C
#cd experiments/platform_controls
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 4A
#cd experiments/stem_loop_buffering
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 4B
# needs table from experiments/platform_controls, should be fine as long as 2C run before 4B...?
#cd experiments/drug_buffering
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 4C
#cd experiments/synthetic_uorf_buffering
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 5B
# uses plotrix library, perhaps an issue?
#cd #cd experiments/d_stall_repressiveness
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 5C
# uses plotrix library, perhaps an issue?
#cd experiments/d_stall_buffering
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 6
# uses plotrix library, perhaps an issue?
#cd #cd experiments/human_uorfs
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# simulations

# Note that we should first analyze the experimental data and copy it to the
# relevant directory before running the analyze_results.Rmd script. Otherwise
# the script does not find data outside its parent directory

# figure 2D
cd modeling/simulation_runs/80s_hit_model_fitting
snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS
cd ../queuing_dissociation_models_fitting
snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figures 3A, 3C, 3D, S2C, S2E, S2F
cd ../constitutive_queuing_dissociation_models_buffering
snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figures 3B, S2A, S2B, S3B
cd ../80s_hit_model_buffering
snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figures 3E, S3A
cd ../regulated_reinitiation_model_buffering
snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 5A
cd ../backward_scanning_d_stall_periodicity
snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure S2D
cd ../backward_scanning_buffering
snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS