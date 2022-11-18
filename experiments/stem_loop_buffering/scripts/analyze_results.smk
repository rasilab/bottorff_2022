# For running simulations in a singularity container
container: "../../../bottorff_2022.sif"

rule all:
  """Analyze experiments and make plots"""
  output:
    "../figures/fig_5a.pdf"
  conda: "R"
  shell:
    """
    Rscript -e "rmarkdown::render('analyze_results.Rmd')"
    """