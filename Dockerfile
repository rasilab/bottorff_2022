# Docker container with conda
FROM continuumio/miniconda3:4.12.0

# install mamba to speed up installs
RUN conda install -c conda-forge -y mamba

# Set up python conda environment
RUN mamba create -y -n py 
RUN mamba install -y -n py -c conda-forge -c defaults -c bioconda snakemake \
    jupyter pandas matplotlib ipykernel pyyaml

# Set up R conda environment
RUN mamba create -y -n R
RUN mamba install -y -n R -c conda-forge -c defaults \
    r-tidyverse \
    r-irkernel \
    r-viridis \
    r-devtools \
    r-janitor \
    r-plotrix \
    r-rtracklayer \
    r-GenomicFeatures \
    r-Biostrings \
    r-plyranges

# Set up R jupyter kernel and make it visible to python
ENV PATH="/opt/conda/envs/py/bin:$PATH"
RUN /opt/conda/envs/R/bin/R -s -e "IRkernel::installspec(sys_prefix = T)"
# Set jupyter data dir for discovering kernels
ENV JUPYTER_DATA_DIR="/opt/conda/envs/py/share/jupyter"

# install rasilab R templates
RUN /opt/conda/envs/R/bin/R -s -e "devtools::install_github('rasilab/rasilabRtemplates')"

# Make R visible to python environment
ENV PATH="$PATH:/opt/conda/envs/R/bin"

# Make 'py' as default conda environment
RUN sed -i 's/conda activate base/conda activate py/' /root/.bashrc

# Download NFsim, PySB, and BioNetGen
RUN wget https://github.com/rasilab/nfsim/releases/download/v1.2.2-alpha/NFsim_v1_2_2_alpha_linux.tgz -O nfsim.tar.gz
RUN wget https://github.com/RuleWorld/bionetgen/releases/download/BioNetGen-2.7.1/BioNetGen-2.7.1-linux.tgz -O bionetgen.tar.gz
RUN wget https://github.com/rasilab/pysb/archive/refs/tags/v1.13.3-alpha.tar.gz -O pysb.tar.gz
# Extract the archives
RUN mkdir nfsim && tar -xzf nfsim.tar.gz && rm nfsim.tar.gz && mv NFsim nfsim/
RUN tar -xzf bionetgen.tar.gz && rm bionetgen.tar.gz && mv BioNetGen-2.7.1 bionetgen
RUN tar -xzf pysb.tar.gz && rm pysb.tar.gz && mv pysb-1.13.3-alpha pysb

# Put NFsim and Bionetgen in PATH
ENV PATH=/nfsim:/bionetgen/:$PATH

# Install PySB into python conda environment
RUN conda run -n py pip install -e /pysb/

# Install pysb_ul4 as package to make it available for all modeling
COPY ../tybottorffdocs/modeling/setup.py /install/ul4/
COPY ../tybottorffdocs/modeling/setup.cfg /install/ul4/
COPY ../tybottorffdocs/modeling/pysb_ul4 /install/ul4/pysb_ul4/
RUN conda run -n py pip install -e /install/ul4/