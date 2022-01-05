# Computational Kinetic Modeling of uORF-mediated Translational Regulation <!-- omit in toc -->

- [Software Requirements](#software-requirements)
- [Software Installation](#software-installation)
- [Model Definition](#model-definition)
- [Model Simulation](#model-simulation)

## Software Requirements

To parse and simulate the kinetic model, we use following software:

- [PySB](https://github.com/rasilab/pysb/tree/total_rate/pysb)
- [BioNetGen](https://github.com/RuleWorld/bionetgen)
- [NFsim](https://github.com/rasilab/nfsim/tree/cleanup_output)

To run simulations, we use the `Python` `conda` environment specified in the [python_environment.yml](python_environment.yml) file.

To analyze simulation results, we use the `R` `conda` environment specified in the [R_environment.yml](R_environment.yml) file.

## Software Installation

Above software necessary for modeling can be installed by creating a [`Docker`]() container from [Dockerfile](Dockerfile). See [Dockerfile](Dockerfile) for how each software is installed. 

    docker build -t bottorff_2022 .

You can then run the container interactively from a `bash` shell using:

    docker run -it --rm -v $(pwd):/modeling -w /modeling bottorff_2022 /bin/bash

To create and run [Docker](https://docs.docker.com/get-started/overview/) containers, follow instructions [here](https://docs.docker.com/engine/reference/commandline/docker/).

## Model Definition

## Model Simulation
