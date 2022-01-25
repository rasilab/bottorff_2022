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
#cd experiments/luciferase_assays/20190422_exp2_ul4_mutants
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 4A
#cd experiments/luciferase_assays/20191223_exps_4_strong_uorf2_gapdh_reduced_init_6_stem_loops_P22A
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 4B
# needs table from experiments/luciferase_assays/20190422_exp2_ul4_mutants, should be fine as long as 2C run before 4B...?
#cd experiments/luciferase_assays/20201121_exp15_4er1cat_wt_p22a_nluc_pest
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 4C
#cd experiments/luciferase_assays/20191021_exp1_K10Q_S12P_exp4_GAPDH_Kozak_mutations
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 5B
# uses plotrix library, perhaps an issue?
#cd #cd experiments/luciferase_assays/20190829_exp4_early_gapdh_stop_no_start_exp5_eYFP_longer_uORF2_exp6_stem_loops
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 5C
# uses plotrix library, perhaps an issue?
#cd experiments/luciferase_assays/20201006_exps_4_gapdh_p22a_strong_d_stall
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 6
# uses plotrix library, perhaps an issue?
#cd #cd experiments/luciferase_assays/20200927_exp18_p22a_wt_no_aug
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# simulations

# Note that we should first analyze the experimental data and copy it to the
# relevant directory before running the analyze_results.ipynb script. Otherwise
# the script does not find data outside its parent directory

# figure 2D
#cd modeling/simulation_runs/0c_andreev_vary_params_for_fitting_controls
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS
cd modeling/simulation_runs/0a_ivanov_geballe_models_vary_reinit_init_for_fitting_controls/
snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figures 3A, 3C, 3D, S2C, S2E, S2F
#cd modeling/simulation_runs/0e_constitutive_ivanov_geballe_buffering
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figures 3B, S2A, S2B, S3B
#cd modeling/simulation_runs/0f_andreev_buffering
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figures 3E, S3A
#cd modeling/simulation_runs/0g_hinnebusch_buffering
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure 5A
#cd modeling/simulation_runs/0l_backwards_scanning_d_stall_periodicity
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS

# figure S2D
#cd modeling/simulation_runs/0j_backwards_scanning_buffering
#snakemake $CLUSTER_ARGS "$SLURM_COMMAND" $SINGULARITY_ARGS