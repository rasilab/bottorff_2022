# Translational buffering by ribosome stalling in upstream open reading frames <!-- omit in toc -->

**Ty Bottorff**<sup>1,2</sup>, **Adam P. Geballe**<sup>3,†</sup>, **Arvind Rasi
Subramaniam**<sup>1,†</sup>

<sup>1</sup> Basic Sciences Division and Computational Biology Section of the
Public Health Sciences Division, Fred Hutchinson Cancer Research Center, Seattle
<br/>
<sup>2</sup> Biological Physics, Structure and Design Graduate Program,
University of Washington, Seattle <br/>
<sup>3</sup> Human Biology Division and Clinical Research Division, Fred
Hutchinson Cancer Research Center, Seattle <br/>

<sup>†</sup>Corresponding authors: A.P.G: <ageballe@fredhutch.org>, A.R.S:
<rasi@fredhutch.org>

bioRxiv 2022.01.06.475296; doi: https://doi.org/10.1101/2022.01.06.475296

**Contents**
- [Abstract](#abstract)
- [Software Installation](#software-installation)
- [Reproducing Simulations and Analyses](#reproducing-simulations-and-analyses)
  - [Desktop computer](#desktop-computer)
  - [Fred Hutch computing cluster](#fred-hutch-computing-cluster)

## Abstract

Upstream open reading frames (uORFs) are present in over half of all human
mRNAs. uORFs can potently regulate the translation of downstream open reading
frames by several mechanisms: siphoning of scanning ribosomes, regulating
re-initiation, and allowing interactions between scanning and elongating
ribosomes. However, the consequences of these different mechanisms for the
regulation of protein expression remain incompletely understood. Here, we
performed systematic measurements on the uORF-containing 5′ UTR of the
cytomegaloviral *UL4* mRNA to test alternative models of uORF-mediated
regulation in human cells. We find that a terminal diproline-dependent
elongating ribosome stall in the *UL4* uORF prevents decreases in main ORF
translation when ribosome loading onto the mRNA is reduced. This uORF-mediated
buffering is insensitive to the location of the ribosome stall along the uORF.
Computational kinetic modeling based on our measurements suggests that scanning
ribosomes dissociate rather than queue when they collide with stalled elongating
ribosomes within the *UL4* uORF. We identify several human uORFs that repress
main ORF translation via a similar terminal diproline motif. We propose that
ribosome stalls in uORFs provide a general mechanism for buffering against
reductions in main ORF translation during stress and developmental transitions.

## Software Installation

Software for running simulations and analyzing results are specified in
[Dockerfile](Dockerfile). The software environment can be recreated by
installing [Docker](https://docs.docker.com/engine/install/) and running the
following command:

```bash
docker build -t bottorff_2022 .
```

An image of the above Docker build is provided as a GitHub package
[here](https://github.com/rasilab/bottorff_2022/pkgs/container/bottorff_2022).

Alternately, opening this folder in [VScode](https://code.visualstudio.com/)
editor with the [Remote -
Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
extension will automatically generate the above Docker image and mount this
folder, provided you have Docker installed. See instructions
[here](https://code.visualstudio.com/docs/remote/containers).

## Reproducing Simulations and Analyses

### Desktop computer

To reproduce all simulations and analyses in the paper, run the following:

```bash
docker run --rm -it -v $(pwd):/workspace bottorff_2022 /bin/bash
cd workspace 
sh run_everything.sh
```

The last above command will take a very long time to run (days or weeks depending on your computer).
Instead, you will likely want to open subfolders for specific experiments or simulations and run the scripts separately there in
the above created Docker environment.
For example, run the following to recreate figure 5B:

```bash
docker run --rm -it -v $(pwd):/workspace bottorff_2022 /bin/bash
cd workspace/experiments/drug_buffering/scripts
snakemake -p --cores=8
```

See [run_everything.sh](run_everything.sh) for which folders correspond to which figures in the manuscript (included as comments).

### Fred Hutch computing cluster

On the Fred Hutch computing cluster, we reproduce the simulations using
[Singularity](https://sylabs.io/guides/3.5/user-guide/introduction.html)
containers and [Slurm](https://slurm.schedmd.com/documentation.html) workload
manager as follows:

```bash
mkdir -p /fh/scratch/delete90/subramaniam_a/user/tbottorf/git/
cd /fh/scratch/delete90/subramaniam_a/user/tbottorf/git/
# clone this repo and go inside
git clone git@github.com:rasilab/bottorff_2022.git
cd bottorff_2022
# load singularity module
module purge
module load Singularity
# pull docker image from GitHub and convert to .sif file 
singularity pull docker://ghcr.io/rasilab/bottorff_2022
# initialize shell
conda init bash
# this conda environment contains snakemake-minimal and pandas and has to be
# outside the Singularity container since it cannot call singularity otherwise
conda activate snakemake
# run everything with singularity and slurm
# see run_everything.sh for details on what the two arguments do
sh run_everything.sh --use-singularity --use-cluster
```

To recreate figures 4A, 4C, 4D, S2C, S2E, S2F specifically, we run:

```bash
mkdir -p /fh/scratch/delete90/subramaniam_a/user/tbottorf/git/
cd /fh/scratch/delete90/subramaniam_a/user/tbottorf/git/
# clone this repo and go inside
git clone git@github.com:rasilab/bottorff_2022.git
cd bottorff_2022/simulation_runs/computational/constitutive_queuing_dissociation_models_buffering
mkdir output
# load singularity module
module purge
module load Singularity
# pull docker image from GitHub and convert to .sif file 
singularity pull docker://ghcr.io/rasilab/bottorff_2022
# initialize shell
conda init bash
# this conda environment contains snakemake-minimal and pandas and has to be
# outside the Singularity container since it cannot call singularity otherwise
conda activate snakemake
snakemake -p --cores=8
```

Again, see [run_everything.sh](run_everything.sh) for which folders correspond to which figures in the manuscript (included as comments).