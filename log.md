```bash
Performing experimental analyses
Building DAG of jobs...
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Using shell: /bin/bash
Provided cores: 72
Rules claiming more threads will be scaled down.
Job stats:
job      count    min threads    max threads
-----  -------  -------------  -------------
all          1              1              1
total        1              1              1

Select jobs to execute...

[Fri Nov 18 12:13:39 2022]
rule all:
    output: ../figures/figs_s1b_and_2c.pdf
    jobid: 0
    resources: tmpdir=/tmp


    Rscript -e "rmarkdown::render('analyze_results.Rmd')"
    
FATAL:   could not open image /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: failed to retrieve path for /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: lstat /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: no such file or directory
[Fri Nov 18 12:13:39 2022]
Error in rule all:
    jobid: 0
    output: ../figures/figs_s1b_and_2c.pdf
    conda-env: R
    shell:
        
    Rscript -e "rmarkdown::render('analyze_results.Rmd')"
    
        (one of the commands exited with non-zero exit code; note that snakemake uses bash strict mode!)

Shutting down, this might take some time.
Exiting because a job execution failed. Look above for error message
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Complete log: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/experiments/platform_controls/scripts/.snakemake/log/2022-11-18T121338.469779.snakemake.log
Building DAG of jobs...
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Using shell: /bin/bash
Provided cores: 72
Rules claiming more threads will be scaled down.
Job stats:
job      count    min threads    max threads
-----  -------  -------------  -------------
all          1              1              1
total        1              1              1

Select jobs to execute...

[Fri Nov 18 12:13:42 2022]
rule all:
    output: ../figures/fig_5a.pdf
    jobid: 0
    resources: tmpdir=/tmp


    Rscript -e "rmarkdown::render('analyze_results.Rmd')"
    
FATAL:   could not open image /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: failed to retrieve path for /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: lstat /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: no such file or directory
[Fri Nov 18 12:13:42 2022]
Error in rule all:
    jobid: 0
    output: ../figures/fig_5a.pdf
    conda-env: R
    shell:
        
    Rscript -e "rmarkdown::render('analyze_results.Rmd')"
    
        (one of the commands exited with non-zero exit code; note that snakemake uses bash strict mode!)

Shutting down, this might take some time.
Exiting because a job execution failed. Look above for error message
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Complete log: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/experiments/stem_loop_buffering/scripts/.snakemake/log/2022-11-18T121341.232304.snakemake.log
Building DAG of jobs...
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Using shell: /bin/bash
Provided cores: 72
Rules claiming more threads will be scaled down.
Job stats:
job      count    min threads    max threads
-----  -------  -------------  -------------
all          1              1              1
total        1              1              1

Select jobs to execute...

[Fri Nov 18 12:13:44 2022]
rule all:
    output: ../figures/fig_5b.pdf
    jobid: 0
    resources: tmpdir=/tmp


    Rscript -e "rmarkdown::render('analyze_results.Rmd')"
    
FATAL:   could not open image /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: failed to retrieve path for /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: lstat /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: no such file or directory
[Fri Nov 18 12:13:44 2022]
Error in rule all:
    jobid: 0
    output: ../figures/fig_5b.pdf
    conda-env: R
    shell:
        
    Rscript -e "rmarkdown::render('analyze_results.Rmd')"
    
        (one of the commands exited with non-zero exit code; note that snakemake uses bash strict mode!)

Shutting down, this might take some time.
Exiting because a job execution failed. Look above for error message
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Complete log: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/experiments/drug_buffering/scripts/.snakemake/log/2022-11-18T121343.159995.snakemake.log
Building DAG of jobs...
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Using shell: /bin/bash
Provided cores: 72
Rules claiming more threads will be scaled down.
Job stats:
job      count    min threads    max threads
-----  -------  -------------  -------------
all          1              1              1
total        1              1              1

Select jobs to execute...

[Fri Nov 18 12:13:46 2022]
rule all:
    output: ../figures/fig_5c.pdf
    jobid: 0
    resources: tmpdir=/tmp


    Rscript -e "rmarkdown::render('analyze_results.Rmd')"
    
FATAL:   could not open image /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: failed to retrieve path for /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: lstat /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/bottorff_2022.sif: no such file or directory
[Fri Nov 18 12:13:46 2022]
Error in rule all:
    jobid: 0
    output: ../figures/fig_5c.pdf
    conda-env: R
    shell:
        
    Rscript -e "rmarkdown::render('analyze_results.Rmd')"
    
        (one of the commands exited with non-zero exit code; note that snakemake uses bash strict mode!)

Shutting down, this might take some time.
Exiting because a job execution failed. Look above for error message
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Complete log: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/experiments/synthetic_uorf_buffering/scripts/.snakemake/log/2022-11-18T121345.011801.snakemake.log
Building DAG of jobs...
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Nothing to be done (all requested files are present and up to date).
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Complete log: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/experiments/d_stall_repressiveness/scripts/.snakemake/log/2022-11-18T121346.900260.snakemake.log
Building DAG of jobs...
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Nothing to be done (all requested files are present and up to date).
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Complete log: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/experiments/d_stall_buffering/scripts/.snakemake/log/2022-11-18T121348.627214.snakemake.log
Building DAG of jobs...
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Nothing to be done (all requested files are present and up to date).
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Complete log: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/experiments/human_uorfs/scripts/.snakemake/log/2022-11-18T121350.390092.snakemake.log
Building DAG of jobs...
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Nothing to be done (all requested files are present and up to date).
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Complete log: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/experiments/supplemental_platform_controls/scripts/.snakemake/log/2022-11-18T121352.062813.snakemake.log
Building DAG of jobs...
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Nothing to be done (all requested files are present and up to date).
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Complete log: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/experiments/supplemental_d_stall_repressiveness/scripts/.snakemake/log/2022-11-18T121353.774372.snakemake.log
Performing computational analyses
mkdir: cannot create directory ‘output’: File exists
SyntaxError in line 28 of /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/computational/simulation_runs/80s_hit_model_fitting/analyze_results.smk:
No rule keywords allowed after run/shell/script/notebook/wrapper/template_engine/cwl in rule analyze_data. (analyze_results.smk, line 28)
SyntaxError in line 28 of /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/computational/simulation_runs/queuing_dissociation_models_fitting/analyze_results.smk:
No rule keywords allowed after run/shell/script/notebook/wrapper/template_engine/cwl in rule analyze_data. (analyze_results.smk, line 28)
mkdir: cannot create directory ‘output’: File exists
SyntaxError in line 28 of /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/computational/simulation_runs/constitutive_queuing_dissociation_models_buffering/analyze_results.smk:
No rule keywords allowed after run/shell/script/notebook/wrapper/template_engine/cwl in rule analyze_data. (analyze_results.smk, line 28)
mkdir: cannot create directory ‘output’: File exists
SyntaxError in line 28 of /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/computational/simulation_runs/80s_hit_model_buffering/analyze_results.smk:
No rule keywords allowed after run/shell/script/notebook/wrapper/template_engine/cwl in rule analyze_data. (analyze_results.smk, line 28)
mkdir: cannot create directory ‘output’: File exists
SyntaxError in line 28 of /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/computational/simulation_runs/regulated_reinitiation_model_buffering/analyze_results.smk:
No rule keywords allowed after run/shell/script/notebook/wrapper/template_engine/cwl in rule analyze_data. (analyze_results.smk, line 28)
mkdir: cannot create directory ‘output’: File exists
SyntaxError in line 28 of /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/computational/simulation_runs/backward_scanning_d_stall_periodicity/analyze_results.smk:
No rule keywords allowed after run/shell/script/notebook/wrapper/template_engine/cwl in rule analyze_data. (analyze_results.smk, line 28)
mkdir: cannot create directory ‘output’: File exists
SyntaxError in line 28 of /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/computational/simulation_runs/backward_scanning_buffering/analyze_results.smk:
No rule keywords allowed after run/shell/script/notebook/wrapper/template_engine/cwl in rule analyze_data. (analyze_results.smk, line 28)
Building DAG of jobs...
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Using shell: /bin/bash
Provided cluster nodes: 999
Job stats:
job      count    min threads    max threads
-----  -------  -------------  -------------
all          1              1              1
total        1              1              1

Select jobs to execute...

[Fri Nov 18 12:14:01 2022]
rule all:
    output: ../figures/fig_s5.pdf
    jobid: 0
    resources: tmpdir=/tmp


    Rscript -e "rmarkdown::render('plot_tcpseq_coverage.Rmd')"
    Rscript -e "rmarkdown::render('plot_riboseq_coverage.Rmd')"
    
Submitted job 0 with external jobid 'Submitted batch job 4155389'.
[Fri Nov 18 12:14:11 2022]
Error in rule all:
    jobid: 0
    output: ../figures/fig_s5.pdf
    shell:
        
    Rscript -e "rmarkdown::render('plot_tcpseq_coverage.Rmd')"
    Rscript -e "rmarkdown::render('plot_riboseq_coverage.Rmd')"
    
        (one of the commands exited with non-zero exit code; note that snakemake uses bash strict mode!)
    cluster_jobid: Submitted batch job 4155389

Error executing rule all on cluster (jobid: 0, external: Submitted batch job 4155389, jobscript: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/computational/uorf_ribosome_density/scripts/.snakemake/tmp.4wdc6kbd/snakejob.all.0.sh). For error details see the cluster log and the log files of the involved rule(s).
Shutting down, this might take some time.
Exiting because a job execution failed. Look above for error message
The code used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-code-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-code-changes)'.
The input used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-input-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-input-changes)'.
The params used to generate one or several output files has changed:
    To inspect which output files have changes, run 'snakemake --list-params-changes'.
    To trigger a re-run, use 'snakemake -R $(snakemake --list-params-changes)'.
Complete log: /fh/scratch/delete30/subramaniam_a/tbottorf/git/bottorff_2022/computational/uorf_ribosome_density/scripts/.snakemake/log/2022-11-18T121400.749656.snakemake.log
```