## Experimental workflow

 - open and run the .Rmd files within the scripts subdirectory

## Modeling workflow

### Necessary versions
 - Python >=3.6
 - conda >= 4.10
<!-- guessing for conda version requirement given mine is 4.10.3 -->

### Necessary modules
 - CMake
 - snakemake

### Setup conda environment, load necessary modules
 - in the current directory, run...
```console
conda deactivate
source ./activate
conda activate base
ml CMake
ml snakemake
```
<!-- `conda env create --file pysb.yml` instead of source ./activate file I copied from Rasi? -->

### Create tsv of simulation parameters
 - `cd` to the modeling directory of interest
 - edit the chosen parameters within the choose_simulation_parameters.py file if desired
 - `python choose_simulation_parameters.py` to generate a tsv of simulation parameters

 ### Submit jobs
 - `snakemake -np` to do a dry run of the job submission
 - `sh submit_cluster.sh` to submit jobs