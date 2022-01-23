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

# figure number panel
# cd $WORKSPACE/experiments/plate_reader/EXPERIMENT_NAME
# snakemake

# simulations

# figure 2C
cd modeling/simulation_runs/0a_ivanov_geballe_models_vary_reinit_init_for_fitting_controls/
# Note that we should first analyze the experimental data and copy it to the
# relevant directory before running the analyze_results.ipynb script. Otherwise
# the script does not find data outside its parent directory
snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS