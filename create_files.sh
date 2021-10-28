#!/bin/sh
# would like to consolidate copying using end of pwd = ${PWD##*/}, but I'm not sure of the syntax for calling variable named end of pwd ($${PWD##*/} fails)
# establish base path
base="/fh/fast/subramaniam_a/user/tbottorf/git/bottorff_2022"
# establish luciferase assay paths
luc_assay="/fh/fast/subramaniam_a/user/tbottorf/analysis/luciferase_assays"
platform_controls="20190422_exp2_ul4_mutants"
d_stall_repressiveness="20190829_exp4_early_gapdh_stop_no_start_exp5_eYFP_longer_uORF2_exp6_stem_loops"
d_stall_buffering="20201006_exps_4_gapdh_p22a_strong_d_stall"
human_uorfs="20200927_exp18_p22a_wt_no_aug"
stem_loop_buffering="20191223_exps_4_strong_uorf2_gapdh_reduced_init_6_stem_loops_P22A"
drug_buffering="20201121_exp15_4e1rcat_wt_p22a_nluc_pest"
synthetic_uorf_buffering="20191021_exp1_K10Q_S12P_exp4_GAPDH_Kozak_mutations"
# establish modeling paths
modeling="/fh/fast/subramaniam_a/user/tbottorf/git/tybottorffdocs/modeling"
sim_runs="/fh/fast/subramaniam_a/user/tbottorf/git/tybottorffdocs/modeling/simulation_runs"
andreev_buff="0f_andreev_buffering"
ivanov_geballe_const_buff="0e_constitutive_ivanov_geballe_buffering"
gcn4_buff="0g_hinnebusch_buffering"
andreev_controls="0c_andreev_vary_params_for_fitting_controls"
ivanov_geballe_controls="0a_ivanov_geballe_models_vary_reinit_init_for_fitting_controls"
d_stall="0b_ivanov_geballe_models_d_stall"
# create folders
cd $base
mkdir experiments modeling
cd $base/experiments
mkdir platform_controls d_stall_repressiveness d_stall_buffering human_uorfs stem_loop_buffering drug_buffering synthetic_uorf_buffering
for dir in */; do cd $dir; mkdir annotations rawdata scripts figures tables; cd ../; done
cd $base/modeling
mkdir buffering platform_controls d_stall
cd buffering
mkdir 80s_hit queueing_mediated_enhanced_repression_collision_mediated_40s_dissociation_and_constitutive_repression regulated_reinitiation
cd ../platform_controls
mkdir 80s_hit queueing_mediated_enhanced_repression_and_collision_mediated_40s_dissociation
cd ../d_stall
mkdir queueing_mediated_enhanced_repression_and_collision_mediated_40s_dissociation
cd ../
for dir in */; do cd $dir; for dir in */; do cd $dir; mkdir output figures tables; cd ../; done; cd ../; done
# copy modeling files needed for all models
cd $base/modeling
cp $modeling/*.py ./
cp $modeling/setup.cfg ./
for dir in */; do cd $dir; for dir in */; do cd $dir; cp $sim_runs/$andreev_buff/run_simulation.py ./; cp $sim_runs/$andreev_buff/Snakefile ./; cp $sim_runs/$andreev_buff/submit_cluster.sh ./; cp $sim_runs/$andreev_buff/cluster.yaml ./; cd ../; done; cd ../; done
cp -R $modeling/pysb_ul4 ./pysb_ul4
# copy 80s hit buffering files
cd $base/modeling/buffering/80s_hit
cp $sim_runs/$andreev_buff/analyze_results_ty.Rmd ./analyze_results.Rmd
cp $sim_runs/$andreev_buff/choose_simulation_parameters.py ./
cp $sim_runs/$andreev_buff/sim.params.tsv ./
# copy buffering files for ivanov, geballe, constitutive repression models
cd $base/modeling/buffering/queueing_mediated_enhanced_repression_collision_mediated_40s_dissociation_and_constitutive_repression
cp $sim_runs/$ivanov_geballe_const_buff/analyze_results_ty.Rmd ./analyze_results.Rmd
cp $sim_runs/$ivanov_geballe_const_buff/choose_simulation_parameters.py ./
cp $sim_runs/$ivanov_geballe_const_buff/sim.params.tsv ./
# copy regulated reinitiation buffering files
cd $base/modeling/buffering/regulated_reinitiation
cp $sim_runs/$gcn4_buff/analyze_results_ty.Rmd ./analyze_results.Rmd
cp $sim_runs/$gcn4_buff/choose_simulation_parameters.py ./
cp $sim_runs/$gcn4_buff/sim.params.tsv ./
# copy 80s hit platform control files
cd $base/modeling/platform_controls/80s_hit
cp $sim_runs/$andreev_controls/analyze_results_ty.Rmd ./analyze_results.Rmd
cp $sim_runs/$andreev_controls/choose_simulation_parameters.py ./
cp $sim_runs/$andreev_controls/sim.params.tsv ./
# copy ivanov and geballe platform control files
cd $base/modeling/platform_controls/queueing_mediated_enhanced_repression_and_collision_mediated_40s_dissociation
cp $sim_runs/$ivanov_geballe_controls/analyze_results_ty.Rmd ./analyze_results.Rmd
cp $sim_runs/$ivanov_geballe_controls/choose_simulation_parameters.py ./
cp $sim_runs/$ivanov_geballe_controls/sim.params.tsv ./
# copy ivanov and geballe d_stall files
cd $base/modeling/d_stall/queueing_mediated_enhanced_repression_and_collision_mediated_40s_dissociation
cp $sim_runs/$d_stall/analyze_results_ty.Rmd ./analyze_results.Rmd
cp $sim_runs/$d_stall/choose_simulation_parameters.py ./
cp $sim_runs/$d_stall/sim.params.tsv ./
# copy platform control files
cd $base/experiments/platform_controls/
cp $luc_assay/$platform_controls/annotations/sampleannotations.csv ./annotations
cp $luc_assay/$platform_controls/scripts/analyze_luminescence_ty.Rmd ./scripts/analyze_luminescence.Rmd
cp $luc_assay/$platform_controls/rawdata/20190422_fluc_nluc.csv ./rawdata
cp $luc_assay/$platform_controls/tables/nluc_fluc_control_mutants_not_normalized.csv ./tables
cp $luc_assay/$platform_controls/tables/nluc_fluc_control_mutants.csv ./tables
# copy d_stall repressiveness files
cd $base/experiments/d_stall_repressiveness/
cp $luc_assay/$d_stall_repressiveness/annotations/sampleannotations.csv ./annotations
cp $luc_assay/$d_stall_repressiveness/scripts/analyze_luminescence_ty.Rmd ./scripts/analyze_luminescence.Rmd
cp $luc_assay/$d_stall_repressiveness/rawdata/20190829_fluc_nluc.csv ./rawdata
# copy d_stall buffering files
cd $base/experiments/d_stall_buffering/
cp $luc_assay/$d_stall_buffering/annotations/sampleannotations.tsv ./annotations
cp $luc_assay/$d_stall_buffering/scripts/analyze_luminescence.Rmd ./scripts
cp $luc_assay/$d_stall_buffering/rawdata/20201006_fluc_nluc.tsv ./rawdata
# copy human uORF files
cd $base/experiments/human_uorfs/
cp $luc_assay/$human_uorfs/annotations/sampleannotations.tsv ./annotations
cp $luc_assay/$human_uorfs/scripts/analyze_luminescence_ty.Rmd ./scripts/analyze_luminescence.Rmd
cp $luc_assay/$human_uorfs/rawdata/20200927_fluc_nluc.tsv ./rawdata
# copy stem loop buffering files
cd $base/experiments/stem_loop_buffering/
cp $luc_assay/$stem_loop_buffering/annotations/sampleannotations.tsv ./annotations
cp $luc_assay/$stem_loop_buffering/scripts/analyze_luminescence_ty.Rmd ./scripts/analyze_luminescence.Rmd
cp $luc_assay/$stem_loop_buffering/rawdata/20191223_fluc_nluc.tsv ./rawdata
# copy drug buffering files
cd $base/experiments/drug_buffering/
cp $luc_assay/$drug_buffering/annotations/sampleannotations.tsv ./annotations
cp $luc_assay/$drug_buffering/scripts/analyze_luminescence_ty.Rmd ./scripts/analyze_luminescence.Rmd
cp $luc_assay/$drug_buffering/rawdata/20201121_fluc_nluc.tsv ./rawdata
# copy synthetic uorf buffering files
cd $base/experiments/synthetic_uorf_buffering/
cp $luc_assay/$synthetic_uorf_buffering/annotations/sampleannotations.tsv ./annotations
cp $luc_assay/$synthetic_uorf_buffering/scripts/analyze_luminescence_ty.Rmd ./scripts/analyze_luminescence.Rmd
cp $luc_assay/$synthetic_uorf_buffering/rawdata/20191021_fluc_nluc.tsv ./rawdata
# replace irrelevant cluster account name, doesn't work yet
find . -type f -name "*.Rmd" -print0 | xargs -0 sed -i 's#"account" : "rasi"#"account" : "account_name"#g'
# replace irrelevant python path with generic
cd $base
find . -type f -name "Snakefile" -print0 | xargs -0 sed -i 's#/fh/fast/subramaniam_a/user/rasi/lib/miniconda3/bin/python#/path/to/python#g'
# replace broken .Rmd links with working ones
find . -type f -name "*.Rmd" -print0 | xargs -0 sed -i 's#"/fh/fast/subramaniam_a/user/tbottorf/analysis/luciferase_assays/20190422_exp2_ul4_mutants/tables/nluc_fluc_control_mutants.csv"#../../../experiments/platform_controls/tables/nluc_fluc_control_mutants.csv#g'
# need to do this after above line
find . -type f -name "*.Rmd" -print0 | xargs -0 sed -i 's#20190422_exp2_ul4_mutants#platform_controls#g'
