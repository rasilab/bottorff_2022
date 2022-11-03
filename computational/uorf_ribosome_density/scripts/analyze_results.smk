# For running simulations in a singularity container
container: "../../../bottorff_2022.sif"

rule all:
  """Analyze experiments and make plots"""
  output:
    "../figures/fig_s5.pdf"
  conda: "R"
  shell:
    """
    Rscript -e "rmarkdown::render('plot_tcpseq_coverage.Rmd')"
    Rscript -e "rmarkdown::render('plot_riboseq_coverage.Rmd')"
    """