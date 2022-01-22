# Docker container with conda
FROM continuumio/miniconda3:4.10.3

# Download NFsim, PySB, and BioNetGen
RUN wget https://github.com/RuleWorld/nfsim/releases/download/v1.2.0/NFsim_v1_2_linux.tgz -O nfsim.tar.gz
RUN wget https://github.com/RuleWorld/bionetgen/releases/download/BioNetGen-2.7.1/BioNetGen-2.7.1-linux.tgz -O bionetgen.tar.gz
RUN wget https://github.com/rasilab/pysb/archive/refs/tags/v1.13.3-alpha.tar.gz -O pysb.tar.gz
# Extract the archives
RUN tar -xzf nfsim.tar.gz && rm nfsim.tar.gz && mv NFsim_v1_3 nfsim
RUN tar -xzf bionetgen.tar.gz && rm bionetgen.tar.gz && mv BioNetGen-2.7.1 bionetgen
RUN tar -xzf pysb.tar.gz && rm pysb.tar.gz && mv pysb-1.13.3-alpha pysb

# Put NFsim and Bionetgen in PATH
ENV PATH=/nfsim:/bionetgen/:$PATH

# Set up python conda environment
COPY .install/python_environment.yml /install/python_environment.yml
RUN conda env create -f /install/python_environment.yml

# Install PySB into python conda environment
RUN conda run -n py pip install -e /pysb/

# Set up R conda environment
COPY .install/R_environment.yml /install/R_environment.yml
RUN conda env create -f /install/R_environment.yml
# Set up R jupyter kernel and make it visible to python
ENV PATH="$PATH:/opt/conda/envs/py/bin"
RUN /opt/conda/envs/R/bin/R -s -e "IRkernel::installspec()"

# Set up shell for conda activation
RUN eval "$(conda shell.bash hook)"

# Install pysb_ul4 as package to make it available for all modeling
COPY modeling/setup.py /install/ul4/
COPY modeling/setup.cfg /install/ul4/
COPY modeling/pysb_ul4 /install/ul4/pysb_ul4/
RUN conda run -n py pip install -e /install/ul4/

# Make R visible to python environment
ENV PATH="$PATH:/opt/conda/envs/R/bin"