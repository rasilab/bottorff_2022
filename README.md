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

```sh
docker build -t bottorff_2022 .
```

Alternately, opening this folder in [VScode](https://code.visualstudio.com/)
editor with the [Remote -
Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
extension will automatically generate the above Docker image and mount this
folder, provided you have Docker installed. See instructions
[here](https://code.visualstudio.com/docs/remote/containers).

## Reproducing Simulations and Analyses

To reproduce all simulations and analyses in the paper, run the following:

```sh
docker run --rm -it -v $(pwd):/workspace bottorff_2022 sh run_everything.sh
```

The above command will take a very long time to run (days or weeks depending on
your computer). Instead, you will likely want to open subfolders for specific
experiments or simulations and run the scripts separately there in the above
created Docker environment. See README.md in [experiments](./experiments) and
[modeling](./modeling) folders for further information. See
[run_everything.sh](run_everything.sh) for which folders correspond to which
figures in the manuscript (included as comments).