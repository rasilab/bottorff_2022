# Docker container with Debian, g++, make, CMake
FROM rikorose/gcc-cmake:gcc-9

# Download NFsim, PySB, and BioNetGen
RUN wget https://github.com/rasilab/nfsim/archive/refs/tags/v1.13-alpha.0.tar.gz -O nfsim.tar.gz
RUN wget https://github.com/RuleWorld/bionetgen/archive/refs/tags/BioNetGen-2.7.0.tar.gz -O bionetgen.tar.gz
RUN wget https://github.com/rasilab/pysb/archive/refs/tags/v1.13.3-alpha.tar.gz -O pysb.tar.gz
# Extract the archives
RUN tar -xzf nfsim.tar.gz && rm nfsim.tar.gz && mv nfsim-1.13-alpha.0 nfsim
RUN tar -xzf bionetgen.tar.gz && rm bionetgen.tar.gz && mv bionetgen-BioNetGen-2.7.0 bionetgen
RUN tar -xzf pysb.tar.gz && rm pysb.tar.gz && mv pysb-1.13.3-alpha pysb

# Compile NFsim
RUN cd nfsim && mkdir build && cd build && cmake .. && make && cd /
# Put NFsim in PATH
ENV PATH=nfsim/build:$PATH

# Install conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.10.3-Linux-x86_64.sh -O miniconda.sh
RUN bash miniconda.sh -b -p /opt/conda
# Put conda in PATH 
ENV CONDA_DIR /opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

# Copy Python and R spec files into container
ADD R_environment.yml /install/R_environment.yml
ADD python_environment.yml /install/python_environment.yml
# Install Python and R conda environments
RUN conda env create -f /install/R_environment.yml
RUN conda env create -f /install/python_environment.yml

# Install PySB into python conda environment
RUN conda run -n py pip install -e /pysb/

# Set up shell for conda activation
RUN eval "$(conda shell.bash hook)"