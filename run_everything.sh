WORKSPACE="."
# experiments

# figure number panel
cd $WORKSPACE/experiments/plate_reader/EXPERIMENT_NAME
snakemake

# simulations

# figure number panel
cd $WORKSPACE/simulation/simulations_runs/SIMULATION_NAME
snakemake