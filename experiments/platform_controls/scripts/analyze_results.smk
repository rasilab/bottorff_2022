# For running simulations in a singularity container
container: "../../../bottorff_2022.sif"

rule all:
  """Analyze experiments and make plots"""
  output:
    "../figures/figs_s1b_and_2c.pdf"
  conda: "R"
  shell:
    """
    Rscript -e "rmarkdown::render('analyze_results.Rmd')"
    """