# Computational Kinetic Modeling of uORF-mediated Translational Regulation <!-- omit in toc -->

- [Software Requirements](#software-requirements)
- [Software Installation](#software-installation)
- [Model Definition](#model-definition)
- [Model Simulation](#model-simulation)

## Software Requirements

To parse and simulate the kinetic model, we use following software:

To run simulations, we use the `Python` `conda` environment specified in the [python_environment.yml](python_environment.yml) file.

To analyze simulation results, we use the `R` `conda` environment specified in the [R_environment.yml](R_environment.yml) file.

## Software Installation

Above software necessary for modeling can be installed by creating a [`Docker`]() container from [Dockerfile](Dockerfile). See [Dockerfile](Dockerfile) for how each software is installed.

    docker build -t bottorff_2022 .

You can then run the container interactively from a `bash` shell using:

    docker run -it --rm -v $(pwd):/modeling -w /modeling bottorff_2022 /bin/bash

## Model Definition

## Model Simulation
