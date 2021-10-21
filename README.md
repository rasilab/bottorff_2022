---
title: Translational buffering by elongation stalls in upstream open reading frames
bibliography: bibliography.yaml
csl: nature.csl
link-citations: true
pandoc_args: ["--filter", "pandoc-fignos"]
fignos-plus-name: Fig.
export_on_save:
  html: true
geometry:
- margin=0.75in
linestretch: 1.2
mainfont: Helvetica
fontsize: 11pt
header-includes:
  - \usepackage[left]{lineno}
  - \linenumbers
  - \usepackage[font=footnotesize,labelfont=bf]{caption}
  - \captionsetup{labelformat=empty}
linkcolor: blue
---

Ty Bottorff^1,2^, Adam P. Geballe^3^, Arvind Rasi Subramaniam^1,†^

^1^ Basic Sciences Division and Computational Biology Section of the Public Health Sciences Division,
^2^ University of Washington Biological Physics, Structure and Design,
^3^ Human Biology Division and Clinical Research Division, 
Fred Hutchinson Cancer Research Center, Seattle, WA 98109, USA  
 ^†^ Corresponding author: A.R.S: <rasi@fredhutch.org>

## Abstract
<!-- Need to be consistent with tenses throughout entire paper... maybe methods is exception
Run entire thing through spell checker -->
Upstream open reading frames (uORFs) are present in over half of all human mRNAs.
uORFs can potently regulate the translation of downstream open reading frames by several mechanisms including siphoning off scanning ribosomes, regulating re-initiation, and changing interactions between scanning and elongating ribosomes.
However, the consequences of these different mechanisms for regulation of protein expression remain incompletely understood.
Here, we performed systematic measurements on the uORF-containing 5′ UTR of the cytomegaloviral *UL4* mRNA to test alternative models of uORF-mediated regulation in human cells.
We find that a terminal diproline-dependent elongation stall in the *UL4* uORF prevents decreases in main ORF translation when ribosome loading onto the mRNA is reduced.
This uORF-mediated buffering is insensitive to the location of the elongation stall along the uORF.
Computational kinetic modeling based on our measurements suggests that scanning ribosomes dissociate rather than queue when they collide with stalled elongating ribosomes within the *UL4* uORF.
We identify several human uORFs that repress main ORF translation via a similar terminal diproline motif.
We propose that elongation stalls in uORFs provide a general mechanism for buffering against reductions in main ORF translation during stress and developmental transitions.

<!-- ## Author summary

Cells require proteins to perform nearly all life functions.
Cells\' needs for proteins change depending on the cell type and growth environment, so protein synthesis is a highly regulated process.
The DNA code within cells specifies what specific functions a cell requires of its proteins.
mRNA molecules are messengers of the genetic code within DNA; mRNA molecules relay this DNA code to protein-making molecular machines called the ribosomes.
Ribosomes load onto mRNA molecules and unidirectionally translate sections of code, open reading frames, to make proteins.
Translation of one open reading frame synthesizes one protein.
The rate of protein synthesis can be varied to change the concentration of proteins within a cell.
One way to regulate the rate of protein synthesis is to vary the rate at which ribosomes load onto mRNA molecules.
One would expect that increasing this ribosome loading rate always increases protein synthesis.
However, in some cases, increasing the rate of ribosome loading onto mRNA molecules can decrease protein synthesis.
This unexpected result can arise in mRNA molecules that have multiple open reading frames from which multiple distinct proteins can be made.
If there are sequences that stall ribosomes within the first encountered open reading frame on an mRNA molecule, then we propose that increasing ribosome loading onto the mRNA molecule can decrease protein synthesis at the second open reading frame.
We find evidence for a model in which ribosomes that collide with a stalled ribosome within the first encountered open reading frame dissociate from, rather than form a queue on, the mRNA molecule.
Our findings have implications for stress-responsive mRNA molecules whose second open reading frames are preferentially translated during cellular stress when this ribosome loading rate is reduced. -->

## Introduction

<!-- ### Eukaryotic translation

Proteins are essential for almost all enzymatic, regulatory, and structural functions within cells.
Accordingly, protein levels must be carefully regulated to maintain homeostasis.
Translation is therefore an essential and heavily regulated biological process.
During translation initiation, ternary complexes (TCs) of eIF2-GTP-Met-tRNA~i~ bind small ribosomal subunits, forming a pre-initiation complex that can bind eIF4F-bound 5\' capped mRNA ends[@Hinnebusch2014].
This pre-initiation complex scans in a 5\' to 3\' direction along the 5\' UTR in search of a start codon.
Once a start codon is selected by the Met-tRNA~i~ anticodon and the associated eIFs, the large ribosomal subunit joins and elongation begins.
The peptide and large ribosomal subunits are released upon termination at a stop codon, yet the small ribosomal subunit may continue scanning and re-initiate translation once a new TC binds[@Bohlen2020]. -->

<!-- ### uORFs are ubiquitous, repressive, and can impart resistance against changes in main ORF translation -->

Translational efficiency can be varied by several mechanisms acting at different stages of mRNA translation.
<!-- For example, translation is globally repressed during the integrated stress response (ISR) by reductions in ribosome loading rates via eIF2α phosphorylation[@Costa-Mattioli2020].
eIF2α phosphorylation inhibits the guanine nucleotide exchange activity of eIF2B and, therefore, impairs TC recycling[@Sudhakar2000].
Aberrantly translated transcripts can also induce quality control pathways to repress their translation[@Joazeiro2019].
Additionally, encoded mRNA sequence features regulate translation efficiency[@Pelletier2019; @Hinnebusch2016]. -->
For example, about half of human mRNAs have at least one upstream open reading frame (uORF) in their 5\' untranslated region[@Wethmar2014; @Ye2015; @Calvo2009]; uORFs have the potential to regulate translation of downsteam ORFs encoding primary gene products.
<!-- uORFs are depleted in housekeeping transcripts and enriched in transcripts coding for membrane proteins, transcription factors, proteins involved in signal transduction, and oncogenes[@Zhang2021]. -->
uORF mutations are implicated in human disease via changes to main ORF translation[@Lee2021]; uORF loss or gain of function mutations in oncogenes or tumor suppressors, respectively, can drive cancer[@Schulz2018; @Smith2021].
Ribosome profiling estimates that about twenty percent of transcripts with uORFs contain actively translated uORFs[@Johnstone2016; @Rodriguez2019] although this estimate may not include weakly translated uORFs.
<!-- Read these papers to get an easier to interpret # here: % of uORFs that are translated? -->
uORFs can regulate gene expression via the biological activity of the uORF peptide, but their regulation usually derives from *cis*-regulation of main ORF translation[@Chen2020; @Zhang2021].
Despite generally having poor initiation sequence contexts, eukaryotic uORFs usually repress main ORF translation, and uORF start codons are therefore often under purifying selective pressure[@Giess2019; @Chew2016; @Kozak1987; @Calvo2009; @Johnstone2016; @Dvir2013; @Wethmar2014; @Zhang2021].
Investigations of uORFs shed light on human health given their abundance in human transcripts and potential to regulate main ORF translation.
<!-- ### uORFs can buffer against changes in main ORF translation -->

While uORFs generally repress main ORF translation, they are also enriched in transcripts resistant to globally reduced ribosome loading resulting from activation of the integrated stress response (ISR) and eIF2α phosphorylation[@Andreev2015; @Sidrauski2015].
For a transcript to be resistant to repressed translation due to reduced ribosome loading, translation at the main ORF of the transcript must decrease less than expected, or even increase, when ribosome loading onto the mRNA is reduced.
<!-- I wonder if we should clarify that translational buffering is also used to describe changes in ribosome protected fragments not from changes in ribosome occupancy but rather from changes in [RNA]
less than "expected" is hard to define here... -->
uORFs have similarly been shown to impart resistance against increases in main ORF translation during neuronal differentiation in which Gcn2 is repressed[@Rodriguez2019; @Roffe2013].
<!-- Re-read rodriguez and see if this works as a simpler and more consistent sentence: For example, uORFs have been shown to impart relative increases in main ORF translation during neuronal differentiation when overall translation is inhibited by Gcn2 acitvation -->
However, not all uORFs impart this resistance, and some uORFs impart resistance while others impart preferred translation during stress[@Andreev2015].
It is unclear by what mechanism(s) uORFs provide resistance to reduced ribosome loading in human cells and how the degree to which resistance occurs is substantiated.
<!-- This is poorly worded, but I would like to get more into resistance (flat line in modeling graph) vs. preferential translation (our more strict definition of buffering) -->

<!-- ### Proposed uORF models that can explain uORF buffering ability, and differentiation between models using computational modeling -->
uORFs can conceivably regulate translation via a variety of mechanisms; the relationship between these mechanisms and stress resistance is unclear.
uORFs can siphon away scanning ribosomes from main ORFs, for example by elongating ribosomes not re-initiating after uORF translation.
Multiple uORFs can also interact together in unique ways, such as in the well-established regulated re-initiation model in which uORFs provide resistance to reduced *ATF4*, and perhaps also *ABCE1*, translation due to reduced ribosome loading caused by phosphorylated eIF2α[@Grant1994;@Vattem2004;Silva2021].
However, about 25% of human transcripts only contain a single uORF[@Ye2015], which does not allow this regulated re-initiation model.
Additionally, elongating ribosomes can pause at certain codons due to reduced peptidyl transferase center activity or tRNA abundances; nascent peptide interactions with the ribosome exit tunnel can also induce pauses[@Zhao2021a;@Arpat2020a].
These pauses can occur in translated mammalian uORFs[@Young2016;@Cao1996], raising the possibility of collision-dependent interactions between scanning and elongating ribosomes within uORFs.
For example, scanning ribosomes might dissociate from mRNAs following collisions with 3\' elongating ribosomes, or, perhaps, they do not dissociate but rather form a queue[@Ivanov2018].
Although various uORF regulatory mechanisms have been proposed, these mechanisms have not been carefully compared using computational modeling coupled with experimental data from a reporter system to look for unique consequences on stress resistance or unique sensitivities to uORF parameters, such as stall location.
<!-- Re-read azin1 ivanov paper to see if/how they compared models -->
<!-- One might expect uORF initiation strength-dependent behaviors in these collision-dependent models due to the different behaviors of scanning and elongating ribosomes within transcripts. -->

Computational modeling can help compare these models and inspire new ones.
For example, a computational model predicted that elongating ribosomes that collide with 3\' scanning ribosomes can cause their dissociation from the mRNA[@Andreev2018].
Computational modeling can not only aid in proposing new regulatory mechanisms, such as this 80S-hit dissociation, but can also enable predictions of protein levels and interpretations of experiments.
We aimed to derive accurate, well-defined kinetic models for these proposed uORF regulatory mechanisms to quantitatively predict their effects on uORF stress resistance in human cells.
We strove to identify unique sensitivities among these models for different uORF parameters, namely stall location.

<!-- ### uORF elongation stall-induced ribosome collisions are required for buffering against reductions in main ORF translation with reduced ribosome loading in single uORF transcripts -->
Here, we test predictions from computational modeling of translation using the repressive human cytomegaloviral *UL4* uORF2.
This uORF2 has been shown to contain a terminal diproline-dependent elongation stall in which the uORF2 peptide disrupts peptidyl transferase center activity[@Bhushan2010; @Wilson2016a].
uORF2 repression of translation has been shown to require its elongation stall, which we reaffirm here[@Cao1995; @Degnin1993].
We find that uORF2 provides resistance to reductions in main ORF translation when ribosome loading rates are reduced and that this behavior requires the uORF2 elongation stall.
This elongation stall induces collisions between ribosomes, and we propose that it is these collisions that allow this buffering behavior.
We then direct our focus to distinguish between two proposed fates of scanning ribosomes that collide with elongating ribosomes: queueing or dissociation.
We find that the distance between the uORF start codon and elongation stall does not impact the regulation of translation, which is inconsistent with scanning ribosome queueing.
We therefore propose that single uORF-containing transcripts require elongation stalls for stress resistance and that scanning ribosomes dissociate rather than queue when encountering a 3\' elongation stall.
We also identify several human uORFs that have similar, repressive terminal diproline motifs.

## Results

### Models of uORF regulation of main ORF translation

We surveyed proposed models of uORF regulation of main ORF translation and distinguish between them using a combination of computational modeling and experimental reporter assays.
In the constitutive repression model, uORFs simply siphon away scanning ribosomes from the main ORF since re-initiation frequencies are less than 100% (Fig. [1](#figure-1)A).
In the 80S-hit dissociation model, elongating ribosomes that catch up to and collide with 3\' scanning ribosomes knock the scanning ribosomes off of the mRNA (Fig. [1](#figure-1)B)[@Andreev2018].
In the queuing-mediated enhanced repression model, a stalled elongating ribosome within the uORF causes a queue of scanning ribosomes to form; this queueing can bias scanning ribosomes to initate translation at the uORF rather than leaky scan past it (Fig. [1](#figure-1)C)[@Ivanov2018].
In the collision-mediated 40S dissociation model, scanning ribosomes dissociate if they collide with a 3\' stalled elongating (80S) ribosome (Fig. [1](#figure-1)D)[@Cao1995; @Degnin1993].
Lastly, in the well-established *ATF4* (human homolog of *GCN4*) uORF regulated re-initiation model, re-initiation after uORF1 can lead to initiation at either uORF2 or the main ORF depending on the stress status of the cell (Fig. [1](#figure-1)E)[@Grant1994].
<!-- Add ATF4 specific citation here -->
When cells are stressed and the proportion of eIF2α that is phosphorylated is higher, ribosomes continuing to scan after terminating at uORF1 are less likely to re-initiate at uORF2 and more likely to re-initiate at the main ORF after acquiring a new ternary complex (TC).
<!-- The language differentiating between re-initiation and continuing to scan after termination feels a bit unclear -->

### Establishing a platform to test different models of uORF regulation of main ORF translation

We predicted the effects of different models of uORF regulation of main ORF translation using computational modeling.
We aimed to find unique modeling predictions that would allow us to experimentally distinguish between the different models of uORF regulation.
One of the key modeling parameters we were interested in varying was the rate of ribosome loading the mRNA since this rate is reduced endogenously during a variety of stress responseses, for example via eIF2α phosphorylation[@Costa-Mattioli2020].
<!-- Add in other stress ISR triggers: eIF4 BP, viral IFITs... here and to other mention similar to this one -->
We specify the models using PySB, a rule-based framework[@Lopez2013].
We then parse the model using BioNetGen and infer a reaction dependency graph[@Harris2016].
Next, we stochastically simulate the models using an agent-based Gillespie algorithm within NFSim[@Sneddon2011].
The molecules and reactions within the kinetic model are shown in Fig. [S1](#figure-s1).
A complete description of the computational modeling can be found in the methods section.
We experimentally test predictions from this computational modeling and then return to refine our model specifications.

Here, we use the well-established human cytomegaloviral *UL4* uORF2[@Cao1995] (Fig. [2](#figure-2)A]) as an experimental platform to test computational modeling predictions of different uORF regulatory models (Fig. [1](#figure-1)).
<!-- Does this 1st half format okay with citation/fig? -->
The *UL4* 5\' UTR contains three uORFs: uORF1 slightly reduces uORF2 repressiveness by siphoning scanning ribosomes away from uORF2, and uORF3 is irrelevant for repression[@Cao1995].
uORF2 represses main ORF translation via an elongation stall that is dependent on the uORF2 peptide sequence[@Cao1996].
The two C-terminal proline residues are critical residues for this elongation stall; these residues are poor substrates for nucleophilic attack to generate a peptide bond and also reorient the ribosomal peptidyl transferase center to reduce termination activity[@Wilson2016a].
This elongation stall also depends on the interaction between the nascent peptide and the GGQ motif within eRF1[@Janzen2002].
We insert this uORF2 into a dual-luciferase reporter system (Fig. [2](#figure-2)B).
We first confirm that uORF2 repressiveness scales with its translation and depends on its terminal diproline-dependent elongation stall (Fig. [2](#figure-2)C).
We later vary uORF parameters to distinguish between proposed uORF regulatory models.

We derive relevant model parameters (Table [1](#table-1)) that best fit these control data (Fig. [2](#figure-2)C).
We are able to match control data with our computational modeling (Fig. [2](#figure-2)D, parameters used in Table [1](#table-1)) for all of the single uORF models with elongation stalls (Fig. [1](#figure-1)B-D).
uORF2 is 22 codons long, but we instead model the wild-type uORF2 with a length of 21 codons.
With a length of 21 codons and a stall located 1 codon before the 3\' end of the uORF, the distance from the uORF start codon to the stall, d~stall~, perfectly fits two ribosomes with 30 nt footprints.
<!-- We also could have just put the stall 2 residues back from the terminus, but that is re-doing simulations that I would not love to do unless we think it's a good idea... -->
This precise fit is necessary for stress resistance in the queueing-mediated enhanced repression model (Fig. [3](#figure-3)C), and we hypothesize that the length of uORF2 would evolve to integer multiples of ribosome footprints if queueing-mediated enhanced repression occurred within uORF2.
<!-- We tried to include the constraint that the stronger Kozak uORF initiates translation 20-30 fold better than the wild-type[@Cao1995], but we were not able to fit our control data with this constraint. -->

### Computational modeling predicts that different models of uORF regulation have unique parameters important for buffering

One of the key modeling parameters we were interested in varying was the rate of ribosome loading onto the mRNA since this rate is reduced endogenously during stress responses[@Costa-Mattioli2020].
<!-- Add other situations of reduced ribosome loading... not just stress responses to here and to other mention of "we were interested in..." -->
uORFs are enriched in transcripts resistant to globally reduced ribosome loading[@Andreev2015; @Sidrauski2015]; here, we use the term buffer to describe this effect of main ORF translation decreasing less than expected, or even increasing, with reduced ribosome loading.
<!-- Another note that I'd like help tightening up buffering definition -->
The constitutive repression model does not confer buffering capacity (Fig. [3](#figure-3)A) since the same percent of scanning ribosomes are siphoned away at all ribosome loading rates.
There are, however, 3 proposed uORF regulatory mechanisms (Fig. [3](#figure-3)B-D) that can explain how a single uORF can buffer against reductions in main ORF translation.
Buffering in the 80S-hit model requires strongly initiating, poorly re-initiating uORFs and is stronger with longer uORFs (Fig. [3](#figure-3)B, Fig. [S2](#figure-s2)A), but most eukaryotic uORFs only weakly initiate translation and are short[@Giess2019; @Chew2016; @Kozak1987; @Calvo2009; @Johnstone2016; @Dvir2013; @Wethmar2014].
Buffering in the queuing-mediated enhanced repression model is sensitive to the distance between the uORF start codon and elongation stall, d~stall~, as this distance determines if a queue of homogenously sized ribosomes can productively increase uORF initiation (Fig. [3](#figure-3)C).
d~stall~ must exactly be an integer multiple of the ribosome footprint (30 nt) for buffering to occur unless we vary the parameter l~scan\ capture~: the distance from start codons from which ribosomes can initiate translation.
For example, if ribosomes are able to initiate translation 3 nt away from start codons with an l~scan\ capture~ value of 3 nt, then a d~stall~ value of 63 nt can still allow buffering (Fig. [S2](#figure-s2)B).
Weakly initiating uORFs can confer buffering in this model.
A version of the 80S-hit dissociation model with an elongation stall acquires d~stall~-dependent buffering similar to that in the queuing-mediated enhanced repression model (Fig. [S2](#figure-s2)C).
Additionally, buffering is greatly weakened in this model when *UL4* uORF2 control matched parameters are used (Fig. [S2](#figure-s2)D) due to this model's dependency on strongly initiating, poorly re-initiating uORFs.
For these reasons, we did not further consider the 80S-hit dissociation model.
In the collision-mediated 40S dissociation model, the rate at which scanning ribosomes dissociate is important for buffering (Fig. [3](#figure-3)D); if this rate is too low, the model reduces to the queuing-mediated enhanced repression model.
Weakly initiating uORFs can confer buffering in this model.
Buffering in the regulated re-initiation model is dependent upon multiple uORFs\' initiation strengths and re-initiation fractions (Fig. [3](#figure-3)E); 2 uORFs are necessary for this effect (Fig. [S2](#figure-s2)E).
Since uORF2 from the *UL4* 5\' UTR is necessary and sufficient for repression of main ORF translation, we did not further consider this model.

### *UL4* uORF2 buffers against reductions in main ORF translation from reduced ribosome loading in an elongation stall-dependent manner

One of the perturbations we modeled computationally and that is also varied in cells is the rate of ribosome loading.
For instance, ribosome loading is globally reduced during the integrated stress response via eIF2α phosphorylation[@Costa-Mattioli2020].
We use several methods to reduce ribosome loading experimentally to test if this computationally predicted buffering effect (Fig. [3](#figure-3)B-E) is observed experimentally.
We measure the translational output with wild-type and no-stall uORF2 variants.
We first reduce ribosome loading with stem-loops near the 5\' cap[@Babendure2006] that reduce the rate of 43S-cap-binding[@Kozak1989].
We vary the degree to which ribosome loading is reduced by varying the stem-loop GC content.
These stem-loops were shown to not affect mRNA stability[@Babendure2006].
We also reduce ribosome loading with the drug 4ER1Cat, which disrupts the interaction between the 5\' cap-binding eIF4E and the scaffold eIF4G.
We vary the degree to which ribosome loading is reduced by varying the concentration of 4ER1Cat.
Finally, we add a short, synthetic uORF 5\' to uORF2 to reduce effective ribosome loading by siphoning some scanning ribosomes away from uORF2.
We vary the degree of ribosome siphoning by varying the synthetic uORF Kozak sequence.
Without the elongation stall present, uORF2 behaves as if it were not present at all (Fig. [2](#figure-2)C), which lets us interpret the no-elongation stall data as a readout of ribosome loading.
We expect main ORF translation to be reduced when ribosome loading is reduced.
However, uORF2 with its elongation stall reduces the degree to which main ORF translation is reduced (Fig. [4](#figure-4)A-B) or even increases main ORF translation (Fig. [4](#figure-4)C).
Therefore, we observe computationally predicted buffering and note that the elongation stall within uORF2 is necessary for this effect.

### Variations in the distance between the uORF start codon and elongation stall do not systematically change uORF repressiveness nor buffering as computationally predicted by the collision-mediated 40S dissociation model

Given that the uORF experimentally tested here represses main ORF translation via an elongation stall independent of other uORFs in the 5\' UTR, we narrowed our focus to the queuing-mediated enhanced repression and collision-mediated 40S dissociation models.
We also consider a form of the 80S-hit dissociation model that contains an elongation stall, but this model reduces to the queuing-mediated enhanced repression model (Fig. [S2](#figure-s2)C).
Our computational modeling predicts that the queuing-mediated enhanced repression model is uniquely dependent on the distance between the uORF start codon and elongation stall.
To increase this distance in the human cytomegaloviral uORF2, we add residues from the N-terminus of eYFP directly 3\' to the uORF2 start codon.
We see no systematic changes in translational regulation (Fig. [5](#figure-5)A), inconsistent with predictions from the queueing-mediated enhanced repression model (Fig. [5](#figure-5)B).
Our longest uORF mutant here is somewhat less repressive, but this may be due to changes to the strength of the peptide sequence-sensitive elongation stall or the peptide extending out of the exit tunnel since about 30 residues of nascent peptides lie within the ribosome exit tunnel[@Wilson2016a].
By our computational modeling predictions of the queuing-mediated enhanced repression model, we would expect to see two broadly spaced clusters of main ORF protein output: 1) repressed when this distance is equal to an integer multiple of the ribosome size, and 2) high when this distance is not equal to an integer multiple of the ribosome size (Fig. [5](#figure-5)B).
We do not computationally predict these two broadly spaced clusters in the collision-mediated 40S dissociation model but rather predict a much lower importance of d~stall~ on uORF repressiveness (Fig. [5](#figure-5)C).
We do computationally predict some importance of d~stall~ on uORF repressiveness in the collision-mediated 40S dissociation model because the dissociation rate is low enough to allow rare queueing.
Thus, our experimental data more closely aligns to computational predictions of the collision-mediated 40S dissociation model.

To further distinguish between the queuing-mediated enhanced repression and collision-mediated 40S dissociation models, we investigated if the uORF with an altered d~stall~ could still buffer against reductions in main ORF translation with reduced ribosome loading.
Our computational modeling predicts that, in the queueing-mediated enhanced repression model, uORFs with altered d~stall~ lengths cannot provide buffering (Fig. [3](#figure-3)C) unless scanning ribosomes are able to initiate translation when not positioned over start codons (Fig. [S2](#figure-s2)B).
<!-- We find that increasing initiation at the uORF greatly increases this buffering strength ({+@fig:kozak_buffering}A, top two rows compared to bottom two rows). -->
We find that a longer d~stall~ still has buffering capacity (Fig. [S3](#figure-s3), top two rows compared to bottom two rows).
Since this d~stall~ length was increased by 6 nt, scanning ribosomes would have to be able to initiate translation 6 nt away from start codons, with an l~scan\ capture~ of at least 6 nt, in order to provide buffering (analogous to l~scan\ capture~ of 3 nt allowing buffering with d~stall~ of 63 nt in Fig. [S2](#figure-s2)B).
We have no evidence to support scanning ribosomes being able to initiate translation this distance from start codons.
<!-- Using parameters fit to control data (Fig. [2](#figure-2)D, Table [1](#table-1)), we computationally predict that buffering strength does not change much and decreases in the queuing-mediated enhanced repression and collision-mediated 40S dissociation models, respectively ({+@fig:kozak_buffering}B-C).
Neither prediction matches the experimental data well, but the prediction from the queuing-mediated enhanced repression model more closely matches our experimental data. -->

### Several human uORFs have repressive diproline motifs, like that in *UL4* uORF2

Given the strong elongation stall in the human cytomegaloviral *UL4* uORF2 that is dependent on a terminal diproline motif, we searched for translated human uORFs that also end in diproline motifs.
We searched for uORFs ending in diproline motifs within three databases: a CRISPR-derived database of ORFs essential for growth in induced pluripotent stem cells and human foreskin fibroblasts[@Chen2020], a database integrated from *de novo* transcriptome assembly and ribosome profiling[@Martinez2020], and a database of proteins less than 100 residues in size derived from literature mining, ribosome profiling, and mass spectrometry[@Hao2018].
Roughly 0.3% of uORFs from these databases ended in diproline motifs, which is not very different from the 0.25% expected from chance.
We identify several human transcripts with uORFs with repressive terminal diproline motifs: *C1orf43*, *C15orf59*, *TOR1AIP1*, and *ABCB9* (Fig. [6](#figure-6)).
Unlike the human cytomegaloviral uORF2, these human uORFs still generally repress translation without their terminal diproline motif.

## Discussion

### uORF elongation stall-induced ribosome collisions are required for buffering against reductions in main ORF translation with reduced ribosome loading in single uORF transcripts

While about 30% of human transcripts have more than 1 uORF, which allows the regulated re-initiation model, about 25% of human transcripts have only 1 uORF [@Ye2015].
While uORFs were shown to be enriched in stress-resistant transcripts, not all uORFs impart this resistance[@Andreev2015].
From our data, we propose that single uORF-containing transcripts require uORF elongation stalls to buffer against reductions in main ORF translation that would otherwise be expected to result from reduced ribosome loading. 
There are a variety of residues that may reduce the rate of elongation, either through changes in the activity of the peptidyl transferase, tRNA availabilities, or interactions between the nascent peptide and the ribosome[@Zhao2021a;@Arpat2020a].
uORFs are often short[@Calvo2009] and may therefore be better poised to stall ribosomes; the nascent peptides may be less likely to be released due to interactions with the ribosome.
In our reporter system, we see that uORF elongation stalls are required to buffer against reduced main ORF translation when ribosome loading is reduced.
We propose that it is the collisions between ribosomes 5\' to the elongation stall that allow buffering.
Since we find that uORF2 requires its elongation stall to buffer against reductions in main ORF translation with reduced ribosome loading, we do not have any evidence supporting the 80S-hit dissociation model.
We computationally predict that the queuing-mediated enhanced repression model is uniquely sensitive to the distance between the uORF start codon and elongation stall, which we do not observe experimentally.
We, therefore, propose that scanning ribosomes dissociate rather than queue when encountering a 3\' stalled elongating ribosome, likely mediated by recruited protein factors.
While we have no direct evidence of scanning ribosome dissociation, the loss of scanning ribosomes during ribo-seq preparations may hint at their dissociation *in vivo*.
This dissociation could serve to maintain the free pool of 40S ribosomal subunits while still allowing regulation of main ORF translation.
Collisions between and subsequent dissociation of scanning ribosomes have also recently been proposed in a model of initiation RQC[@Garshott2021].
We are interested in modeling the effects of ribosome depletion on these different models of uORF regulation of main ORF translation.
We have some preliminary data suggesting that RP depletion changes uORF regulation of ATF4 translation.
<!-- Perhaps we should clarify in the discussion that dissociation in this paper likely doesn't mean a spontaneous dissociation but rather a rescue by some (group of) factor(s) -->

### Alternative explanations for single uORF-containing transcript buffering in cells

Cellular stress may enhance start codon fidelity, via phosphorylation of eIF1, which could also allow buffering in single uORF-containing transcripts[@Zach2014; @Young2016a; @Palam2011].
However, start codon fidelity should not change with our synthetic uORF- or stem loop-based reductions in ribosome loading in which we see uORF elongation stall-dependent buffering.

### Why might uORFs generally initiate translation poorly?

Many genome-scale uORF studies have shown that uORFs usually have poor start contexts, both in terms of the Kozak sequence and the choice of a cognate or non-cognate start codon[@Wethmar2014;@Chew2016;@Kozak1987;@Johnstone2016].
uORFs may have evolved to weakly initiate translation to be less repressive of main ORF translation[@Dvir2013;@Chew2016;@Johnstone2016;@Wethmar2014;@Matsui2007].
uORFs may also weakly initiate translation in order to reduce the incidences of nonsense-mediated decay (NMD), a quality control mechanism that degrades mRNAs with premature translation termination that is triggered more often with better-translated uORFs[@Wallace2020;@Aliouat2019;@Jia2020].
Poor uORF initiation contexts may also minimize translation of N-terminal extensions or out-of-frame translation products in cases where uORF stop codons are mutated with uORFs in or out-of-frame with main ORFs, respectively.
<!-- We see here that a stronger uORF initiation does increase the buffering strength ({+@fig:kozak_buffering}A), but this stronger uORF initiation also reduces main ORF translation at all ribosome loading rates. -->
Cells likely balance the benefits of increased buffering strength with the disadvantages of reduced main ORF translation.

### Cells respond to elongation stalls via quality control pathways

We propose that uORF elongation stalls buffer against reductions in main ORF translation with reduced ribosome loading.
However, elongation stalls likely also exist to offer sufficient time for co-translational folding although this is likely more relevant for elongation stalls within main ORFs that have functional peptides[@Collart2020].
Ribosome queues can induce ribosome quality control, such as in the *XBP1* mRNA, in which ZNF598 ubiquitinates collided disomes of elongating ribosomes[@Han2020].
EDF1 binds collided disomes, prevents frameshifting, and stabilizes GIGYF1/2 binding, which recruits 4EHP to outcompete cap eIFs[@Juszkiewicz2020].
Elongation stalls may similarly serve a neuroprotective role by inducing the ISR via GCN2 to globally repress translation and prevent frameshifting[@Terrey2020; @Ishimura2016].
Additionally, elongating ribosome stalls are not all created equal and are differentially treated based on stall type and duration[@Yan2020].
For instance, increasing stall duration switches the response from RQC or NGD, to the ZAKα-GCN2-eIFα phosphorylation integrated stress response, to the ZAKα-MAPKKK-p38-JNK-apoptosis ribotoxic stress response[@Wu2020]
We do not, however, have any evidence of ribosome quality control following elongation stalls in uORF2.
Collisions between scanning and elongating ribosomes and subsequent quality control are not well understood; what we describe as scanning ribosome dissociation here may be rescue by an unknown quality control pathway.
Our computational modeling would predict that this GIGYF1/2-mediated reduced transcript-specific or GCN2-ISR-mediated globally reduced ribosome loading would increase main ORF translation in transcripts with uORF elongation stalls.

### uORFs can sometimes induce changes in mRNA stability
<!-- Redundant with NMD mention above... -->
uORFs may induce nonsense-mediated decay, although that is more likely when they are better-translated with stronger Kozak sequences[@Aliouat2019].
The cytomegaloviral *UL4* uORF2 has been shown to repress main ORF translation in an mRNA-level independent manner, and it also only weakly initiates translation[@Cao1995].
Although some uORF regulation of translation can arise from changes in mRNA stability, we do not believe that the uORF used here regulates translation through changes in mRNA stability.
We have some preliminary evidence that proline-dependent stalls do not trigger mRNA decay as much as other residue-dependent stalls do.

### Viral infections do not always globally repress host translation

The uORF2 tested here is a cytomegaloviral uORF.
Although viral infections generally globally repress host translation, cytomegalovirus infection does not, which begs the question of why the *UL4* uORF2 evolved an elongation stall that buffers against reductions in main ORF translation with reduced ribosome loading.
Vaccinia is another virus that does not induce the ISR.
<!-- Apparently most viruses (like CMV) do what I'm talking about below (1st half of sentence)... read more about viruses... -->
Vaccinia infection suppresses the ISR by antagonizing eIF2α phosphorylation, which renders this infection dependent on ribosome quality control to resolve stalls and maintain the translating ribosome pool[@Sundaramoorthy2020].

### Evidence supporting the queuing-mediated enhanced repression model

Although our data here does not support the queuing-mediated enhanced repression model, others have found evidence that does support this model.
Translation from non-cognate start codons was shown to be resistant to cycloheximide, perhaps due to ribosome queueing, but sensitive to limitations in ribosome loading[@Kearse2019].
Loss of eIF5A, which helps ribosomes clear pauses, was shown to increase 5\' UTR translation in 10% of studied genes in human cells, augmented by downstream in-frame pause sites within 67 codons[@Manjunath2019] although this interpretation may be complicated by eIF5A's role in translation termination[@Schuller2017].
There is also evidence of queueing-enhanced uORF initiation in the 23 nt long *Neurospora crassa* arginine attenuator peptide[@Gaba2020] as well as in transcripts with secondary structure near and 3\' to start codons[@Kozak1989a] although in both of these situations the queue is only one ribosome footprint long.
Stalled ribosomes that only allow scanning ribosomes to scan 3\' enough to just detect a uORF start codon would increase uORF initiation even with a competing dissociation rate.
When the distance between the start codon and the stall is just one ribosome size long, (u)ORF initiation depends on the relative start codon selection and dissociation rates.
When this distance is longer, the dissociation rate holds more weight as the 3\' most scanning ribosome in a queue is not always positioned near a start codon.
The *UL4* cytomegaloviral uORF2 and our modeled uORFs are about two ribosome footprints long, but for uORFs about one ribosome footprint long the queuing-mediated enhanced repression model may be more accurate.
Human uORFs have a median uORF length of 48 nt, which is closest to two ribosome footprint lengths[@Calvo2009].
The only difference between the queuing-mediated enhanced repression and collision-mediated 40S dissociation models is the rate at which scanning ribosomes dissociate when collided with 3\' ribosomes.
This rate may be regulated by associated protein factor binding and may differ between different uORFs due to their different sequences.

### Future directions
<!-- Long and speculative -->
Very few uORFs have been mechanistically characterized[@Wethmar2014].
We are interested in testing other elongation stall-containing uORFs, such as the peptide sequence sensitive uORFs that regulate human methionine synthase[@Col2007] and antizyme inhibitor I[@Ivanov2018].
There are also uORFs in several transcripts found to be preferentially translated during arsenite-induced cellular stress, namely PPP1R15A, SLC35A4, C19orf48, that we would predict to contain elongation stalls[@Andreev2015].
We are also interested in building more complex models that incorporate more reactions that affect translation.
For example, we do not consider 3\' UTR elements, such as the 3\' UTR translational derepression element in the Her-2 transcript that diminishes uORF-mediated repression of main ORF translation in cancerous cells, in our models[@Mehta2006].
We also do not allow scanning ribosomes to scan backward (3\' to 5\') although we do vary the distance from which ribosomes can initiate translation with variations in l~scan\ capture~.
We are also interested in testing the effect of stress-reduced elongation rates[@Sanchez2019], which may regulate uORF-mediated buffering between stressed and non-stressed conditions.
It may also be interesting to test the effect of heterogeneous ribosome footprints across different power strokes and open or occupied A site states during translation[@Wu2019], which likely would reduce both the dependence of the queuing-mediated repression model on d~stall~ and buffering strength.
We are also interested in modeling the translation of a heterogeneous mRNA population since, here, we only simulate the translation of a single mRNA.
Additionally, in our computational modeling, initiation proceeds via a cap-severed mechanism in which multiple scanning ribosomes can be present in the 5\' UTR at the same time.
If we were to model cap-tethered initiation, strong uORF elongation stalls would eventually sever this connection, similar to how the cap-eIF-ribosome connection is severed during the usually longer translation of main ORF, but we have not yet modeled this different mechanism of initiation.

## Author Contributions

T.A.B. designed research, performed computations and experiments, analyzed data, and wrote the manuscript.
A.P.G. conceived the project, designed research, and wrote the manuscript.
A.R.S. conceived the project, designed research, performed computations and experiments, analyzed data, wrote the manuscript, supervised the project, and acquired funding.

## Acknowledgements

We thank members of the Subramaniam lab, the Basic Sciences Division, and the Computational Biology Program at Fred Hutch for assistance with the project and discussions and feedback on the manuscript.
The computations described here were performed on the Fred Hutch Cancer Research Center computing cluster.
This research was funded by NIH R21 AI156152 received by APG and NIH R35 GM119835, NSF MCB 1846521, and the Sidney Kimmel Scholarship received by ARS.
This material is based upon work supported by the National Science Foundation Graduate Research Fellowship Program under Grant No. (NSF DGE-1762114 and DGE-2140004).
Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.
This research was supported by the Genomics Shared Resource of the Fred Hutch/University of Washington Cancer Consortium (P30 CA015704) and Fred Hutch Scientific Computing (NIH grants S10-OD-020069 and S10-OD-028685).
The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

**Competing interests**: None

## Data and Code Availability

Data and analysis code are provided as supplementary files to the manuscript.
These will also be made available as a public GitHub repository prior to publication.

## Materials and Methods

### Plasmid construction

The parent cloning vector was created as follows.
A Promega commercial pGL3 vector with ampicillin resistance was received from Andrew Hsieh (Fred Hutchinson Cancer Research Center).
Nanoluc and firefly luciferase were cloned into this vector.
A downstream multiple cloning site was removed.
Nanoluc expression is driven by a CMV promoter.
Firefly luciferase expression is driven in the opposite direction within the plasmid and serves as an internal transfection control.
The human cytomegaloviral *UL4* 5\' UTR was PCR amplified from a construct gifted from HCMV genomic DNA.
<!-- Need to cite HCMV genomic DNA -->
To create mutant 5\' UTR versions of the parent pGL3-Fluc-Nluc vector, the vector was digested with KpnI/EcoRI unless otherwise noted.
In some cases, this digestion dropped a GFP cassette.
1-2 PCR-amplified fragments with 20-30 bp homology arms were then inserted using isothermal assembly[@Gibson2009].
The stem-loop[@Babendure2006] 5\' UTR mutants were cloned as follows.
The stem-loops were ordered as oligonucleotides with overhangs for ligation into ClaI and NotI sites.
The oligonucleotides were annealed and used in PCR reactions to add CMV homology arms.
An AAVS1 parent vector was digested with ClaI and NotI.
These stem-loops were then inserted into the ClaI/NotI restriction digested parent vector by isothermal assembly[@Gibson2009].
The stem-loops were then PCR amplified off of this plasmid and inserted into the pGL3-Fluc-*UL4*-5\'-UTR-Nluc parent vector described above.
The several tested human uORFs were PCR amplified from human genomic DNA and inserted into a PstI/EcoRI digested parent.
The inserted sequences were confirmed by Sanger sequencing.
Kozak sequence and stall codon mutations were introduced in the PCR primers used for amplifying inserts before isothermal assembly.
Standard molecular biology procedures were used for all other plasmid cloning steps[@Sambrook2001].
Table [S1](#table-s1) lists the plasmids described in this study.
Plasmids will be sent upon request.

### Cell culture

HEK293T cells were cultured in gibco\'s Dulbecco\'s modified Eagle medium (DMEM 1X, REF 11965-092, + 4.5 g/L D-glucose, + L-glutamine, - sodium pyruvate) and passaged using 0.25% trypsin in EDTA (REF 25200-056).

### Dual-luciferase reporter assay
<!-- Review these methods: compare to lab notebook -->
Plasmid constructs were PEI or lipofectamine (Invitrogen Lipofectamine 3000, REF L3000-008) transiently transfected into HEK293T cells for 12-16h in 96, 24, or 12 well plates.
If the plasmids were not transfected into a 96 well plate, then the cells were resuspended in 100 µL media.
Then, 20 µL of cells were added per well to a 96 well plate for the dual-luciferase assay.
If the transfection was already in a 96 well plate, the \~ 110 µL media was removed and replaced with 20 µL media per well.
The Promega dual-luciferase kit was used.
Cells were lysed with 20 µL ONE-Glo EX Luciferase Assay Reagent per well for three minutes to measure firefly (*Photinus pyralis*) luciferase activity.
Then, 20 µL NanoDLR Stop & Glo Reagent was added per well for 10 minutes to quench the firefly luciferase signal and provide the furimazine substrate needed to measure NanoLuc luciferase activity.
Firefly luciferase activity serves as an internal control for transfection efficiency, and Nanoluc activity provides a readout of 5\' UTR regulation of Nanoluc translation.

### Kinetic modeling of eukaryotic translational control

We specify our kinetic models using the PySB interface[@Lopez2013] to the BioNetGen modeling language[@Harris2016].
The exported tasep.py Python script is parsed by BioNetGen into a tasep.bngl file and converted into a tasep.xml file accessible to the agent-based stochastic simulator NFsim[@Sneddon2011].

#### Molecules  

Our kinetic models of eukaryotic translational control describe the interactions between 2 molecule types: mRNA and ribosome.
Here, we describe these molecules\' components, states, and binding partners.
mRNA molecules have the following components: 5\' end and codon sites (*c~i~*).
The mRNA 5\' end can either be free of or occupied with a ribosome.
The mRNA 5\' end must be free for a 43S to bind, which leaves the 5\' end blocked until the ribosome scans (or elongates) sufficiently 3\' downstream.
The mRNA codon sites serve as bonding sites for the ribosome A site.
Ribosomes, both scanning and elongating, have the following components: A site (*a*), 5\' side (*t* for trailing), and 3\' side (*l* for leading).
These sites serve as bonding sites for either the mRNA (A site) or other ribosomes during collisions (5\' or 3\' side).
Both scanning and elongating ribosomes have mRNA footprints of 10 codons in our simulations based on mammalian ribosome profiling data[@Ingolia2011; @Jackson2015].

#### Kinetic reactions  

We describe here each type of kinetic reaction in our models of eukaryotic translational control.
We use a syntax similar to that of BioNetGen[@Harris2016] to illustrate the kinetic reactions.
We scale ternary complex (TC) and ribosome subunit numbers (100 each) to the single mRNA present in the simulation.
Simulation of a single mRNA is sufficient to infer translation dynamics.

##### Initiation  

###### Pre-initiation complex (PIC, 43S) formation  

Small ribosomal subunits must bind TCs to form pre-initiation complexes (PICs, 43Ss) before loading onto mRNAs.
PIC formation is not rate-limiting in our simulations; we set the rate of 43S-cap binding (k~cap\ bind~) to be rate-limiting and a total rate (independent of [43S]) to set the overall initiation rate to that of cellular estimates.
Therefore, we arbitrarily set the second-order PIC formation rate (40S-TC binding rate, k~ssu\ tc\ bind~) to 0.01 * TC^-1^ * SSU^-1^ such that 100 40S-TC binding events occur per second, which is much higher than the rate-limiting cap binding rates.

###### PIC (43S) loading onto mRNA  

Small ribosome subunit loading can occur when the 5\' most 30 nucleotides (nt) of the mRNA are not bound to any ribosomes since we model ribosome footprints at 30 nt following mammalian ribosome profiling data[@Ingolia2011; @Jackson2015].
The rate at which small ribosomal subunits load onto the 5\' end of the mRNA, k~cap\ bind~, is varied about 100-fold beneath a high ribosome loading rate, 0.125/s, based on single-molecule estimations in human cells[@Yan2016].
Small ribosomal subunits can load onto the mRNA when a ribosome footprint-sized region 3\' to the 5\' end is free of ribosomes.
Small ribosomal subunit loading results in the 5\' end being blocked until this ribosome scans or elongates past a ribosome footprint from the 5\' cap.

###### Scanning and start codon selection  

The scanning rate is 5 codons/s following an estimate in a mammalian cell-free translation system[@Vassilenko2011]; this rate was also used in another computational simulation of translation[@Andreev2018].
Unless otherwise stated with variations in the l~scan\ capture~ parameter, small ribosomal subunit A sites must be positioned exactly over start codons to initiate translation.
The uORF start codon is 25 nt from the 5\' cap.
We vary the rate at which this start codon selection occurs at the uORF in our modeling.
Start codon selection releases the TC bound to the small ribosomal subunit.
We do not model TC regeneration via eIF2B.
The start codon selection rate divided by the sum of this start codon selection rate and the scanning rate equals the baseline initiating fraction.
This calculation of the baseline initiating fraction may underestimate the initiating fraction in the case of a correctly positioned 3\' ribosome queues (as in the queuing-mediated enhanced repression model).

##### Elongation  

Elongation results in the ribosome A site moving from codon *c~i~* to codon *c~i+1~*.
The rate of elongation is set to 5 codons/s following single-molecule method and ribosome profiling estimates in mammalian cells of 3-18 codons/s[@Wu2016; @Pichon2016; @Yan2016; @Ingolia2011; @Morisaki2016].
Elongation may only proceed if there is no occluding 3\' ribosome; in other words, elongation may only procceed from codon *c~i~* to codon *c~i+1~* if the next 3\' ribosome\'s A site is bound to a codon no more 5\' than *c~i+11~*.
The elongation rate at the stall within the uORF is set to 0.001/s based on toeprinting assays over time with various inhibitory drugs[@Cao1998].

##### Termination and re-initiation  

Termination results in the dissociation of the large ribosomal subunit, but the small ribosomal subunit may continue scanning and subsequently re-initiate.
<!-- Again re-initiation definitiation vague -->
The termination rate is set to 1/s given that ribosome density tends to be higher at stop codons than within ORFs[@Wu2019; @Ingolia2011].
The recycling rate of terminated small ribosomal subunits after uORF translation is varied to model the effect of re-initiation after uORFs on the regulation of main ORF translation.
The scanning rate divided by the sum of the scanning rate and this recycling rate equals the re-initiation fraction.
Re-initiating small ribosomal subunits must still bind another TC before being able to select a downstream start codon.

##### Collisions and dissociations  

A collision between two ribosomes requires them to be separated by exactly one ribosome footprint in distance on the mRNA and result in bonds between the 5\' side of the leading (3\' most) ribosome and the 3\' side of the trailing (5\' most) ribosome.
Abortive (premature) termination of ribosomes results in their dissociation from the mRNA and any collided ribosomes they are bound to.
Different models have different non-0 dissociation rates.
For instance in the 80S-hit model, the following rates are equal and larger than 0: k~scan\ term\ 5\ hit\ 80s~, k~scan\ term\ both\ hit\ 80\ 80s~, k~scan\ term\ both\ hit\ 80\ 40s~.
These rates relate to the dissociation of scanning ribosomes given collisions with a 5\' elongating ribosome.
In the collision-mediated 40S dissociation model, the following rates are equal and larger than 0: k~scan\ term\ 3\ hit\ 40s~, k~scan\ term\ 3\ hit\ 80s~, k~scan\ term\ both\ hit\ 40s\ 40s~, k~scan\ term\ both\ hit\ 40s\ 80s~, k~scan\ term\ both\ hit\ 80s\ 40s~, k~scan\ term\ both\ hit\ 80s\ 80s~.
These rates relate to the dissociation of scanning ribosomes given collisions with a 3\' scanning or elongating ribosome.
The *in vivo* abortive termination rates are not known.
Small ribosomal subunits that happen to make it to the 3\' end of the mRNA through leaky scanning of all (u)ORFs always dissociate.

### Human uORF search  

We import uORF lists several databases[@Chen2020; @Martinez2020], including the SmProt less than 100 residue protein database of computationally or experimentally identified in multiple cell lines downloaded from <http://bioinfo.ibp.ac.cn/SmProt/download.htm>, and, if needed to derive their peptide sequence via tblastn, map their coordinates to the human genome.
This SmProt database includes 3162 uORFs from ribosome profiling data, which we filter down first to 1080 uORFs after filtering for aligned matches, available Kozak sequence, sensible start codons, and non-duplicates.
Two of these uORFs end in diproline motifs: *C1orf43* and *CHCD5*.
One database is a set of high confidence ORFs derived from ribosome profiling of human-induced pluripotent stem cells (iPSCs) or foreskin fibroblast cells (HFFs) and was downloaded from <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4720255/bin/NIHMS741295-supplement-3.csv>[@Chen2020].
This database includes 1517 high confidence (ORF-RATER score \> 0.8) uORFs from either iPSCs or HFFs, which we filter down to 8 that end in diproline motifs: *ABCB9*, *C1orf43*, *FAM109A*, *GAL3ST3*, *RHOBTB2*, *SLC35A3*, *TOR1AIP1*, and *WDR86*.
The second database derives from HEK293T, HeLa, and K562 cells using ribosome profiling and was downloaded from <https://static-content.springer.com/esm/art%3A10.1038%2Fs41589-019-0425-0/MediaObjects/41589_2019_425_MOESM3_ESM.xlsx>[@Martinez2020].
This database includes 3577 uORFs which we filter down to 15 that end in diproline motifs and that are less than 60 residues in length for ease of cloning: *ABCB9*, *APOO*, *ATG13*, *C15orf59*, *ELGN1*, *HAUS4*, *HES4*, *PIGB*, *PPP1R37*, and *ST13*.
<!-- I need to be consistent for figures with yes/no subfigure titles within figure... -->

\pagebreak

## Figure 1

![
**Models of uORF regulation considered in this study.**  
**(A)** Constitutive repression.  
The uORF constitutively siphons away a proportion of scanning ribosomes from the main ORF.  
**(B)** 80S-hit dissociation.  
Elongating ribosomes that collide with 3′ scanning ribosomes cause the leading scanning ribosome to dissociate from the mRNA.  
**(C)** Traffic jam-mediated enhanced repression.  
Scanning or elongating ribosomes form a queue behind a 3′ stalled elongating ribosome.
If the queue correctly positions a scanning ribosome at the uORF start codon, then the proportion of scanning ribosomes that initiate translation at the uORF increases.  
**(D)** Collide and dissociate.  
Scanning ribosomes that collide with a 3′ stalled elongating ribosome dissociate from the mRNA.  
**(E)** Regulated re-initiation.  
Ribosomes initiate translation at uORF1, and scanning continues after termination.
Ribosomes re-initiate at the main ORF or uORF2 when phosphorylated eIF2α levels are high or low, respectively.
The schematic is depicted in a low phosphorylated eIF2α state.
](svg/main_modeling_schematics.svg){width=5.689in}

\pagebreak

## Figure 2

![
**An experimental and computational platform for assessing uORF-mediated regulation of main ORF translation.**  
**(A)** The 236 nt 5\' UTR of *UL4* mRNA from human cytomegalovirus contains 3 uORFs.  
**(B)** A dual-luciferase reporter system measures 5\' UTR repressiveness in HEK293T cells.  
Firefly luciferase signal serves as an internal control for transient (24h) transfection efficiency.  
**(C)** This reporter system recapitulates the known elongation stall-dependent repression of translation by the *UL4* uORF2[@Cao1996].  
The indicated mutations improve the uORF2 Kozak sequence, remove the start codon, or remove the elongation stall.
Error bars show standard error of mean Nluc / Fluc ratios over 3 technical replicates.
Data are normalized to a no-uORF start codon control.  
**(D)** Computationally predicted uORF regulation in the 80S-hit dissociation, queuing-mediated enhanced repression, and collision-mediated 40S dissociation models.  
Data are normalized to a no-uORF start codon control.
The parameter combination that best recapitulated the control behavior in Fig. [2](#figure-2)C is displayed in Table [1](#table-1).
Error bars of simulated data are smaller than data points.
](svg/main_ul4_5'_utr_dual_luciferase_reporter_system_control_mutants.svg){width=5.215in}

\pagebreak

## Figure 3

![
**Kinetic modeling predicts translational buffering by uORFs.**  
Buffering refers to a less than expected decrease, or even increase, in main ORF translation with reduced ribosome loading.  
<!-- ~Technically, buffering could include a smaller than expected decrease (i.e. a flat line?) -->
**(A)** The constitutive repression model has no buffering behavior.  
In this model, buffering doesn\'t occur at any uORF initiation or re-initiation rates.
uORFs simply siphon away scanning ribosomes from the main ORF.
<!-- (100 - uORF initiation percent) percent ribosomes leaky scan to the main ORF, and uORF initiation percent * re-initiation percent scanning ribosomes initiate and re-initiate to make it to the main ORF. -->
There is no elongation stall in this model.  
**(B)** Buffering in the 80S-hit dissociation model depends on uORF (re-)initiation, among other parameters[@Andreev2018].  
For buffering to occur in this model, uORFs must initiate well in order to have enough elongating ribosomes to hit 3\' scanning ribosomes.
uORFs must also re-initiate poorly; high re-initiation coupled with high uORF initiation allows many scanning ribosomes to make it to the main ORF.
Buffering occurs better with longer uORFs with more room for elongating ribosomes to hit 3\' scanning ribosomes; here, the uORF is 100 residues long.
The dissociation rate is 200/s, so 99% of scanning ribosomes hit by 5\' elongating ribosomes dissociate rather than continue scanning.
The scanning and elongation rates are 2 codons/s.
There is no elongation stall in this model.  
**(C)** Buffering in the queuing-mediated enhanced repression model depends on d~stall~: the distance between the uORF start codon and elongation stall.  
In this model, uORF initiation can increase above baseline with increased ribosome loading when the distance between the uORF start codon and elongation stall is an integer multiple of the ribosome footprint (30 nt).
When this condition is met, buffering occurs.
For d~stall~ values of 60, 63 nt, the uORF length is 21, 22 codons, respectively.  
**(D)** Buffering in the collision-mediated 40S dissociation model depends on the dissociation rate.  
Here, d~stall~ is 63 nt; with a low dissociation rate, this model reduces to the queueing-mediated enhanced repression model.  
**(E)** Buffering in the regulated re-initiation model depends on uORF (re-)initiation.  
In order for buffering to occur, several conditions must be met.  
Both uORFs must be translated well (Fig. [S2](#figure-s2)E); the legend color refers to both uORFs\' initiation.
uORF1 re-initiation must be high.
uORF2 re-initiation must be low.
uORF2 is 3 residues long.
There is no elongation stall in this model.  
uORFs are located 25 nt from the 5\' cap.
Ribosome footprints are 30 nt.
99% of scanning ribosomes that make it to the main ORF will initiate translation; 1% will leaky scan.
Unless otherwise stated, parameters (Table [1](#table-1)) obtained from fitting control data (Fig. [2](#figure-2)C-D) are used here.
Ribosome loading is the k~cap\ bind~ rate for non-regulated re-initiation models.
<!-- I tried modeling the regulated-reinitiation model with variation in k_ssu_tc_bind to get the same x-axis (ribosome loading), and there's no buffering, probably because of the k_ssu_tc_bind not being split into free/mRNA bound, doesn't seem worth the effort at this point... -->
<!-- Ribosome loading is defined as $\dfrac{1}{\dfrac{1}{s*t*k_{1}}+\dfrac{1}{k_{2}}}$ where $k_{1}$ = k~ssu\ tc\ bind~, $k_{2}$ = k~cap\ bind~, $s$ = the number of small ribosomal subunits, and $t$ = the number of ternary complexes, this ~= k_cap_bind for our rate regime -->
We model changes in ribosome loading via changes in k~cap\ bind~ as that rate is easier to match to *in vivo* estimates of ribosome loading.
However, buffering in the regulated re-initiation model is dependent on an eIF2α phosphorylation mechanism; we instead vary the number of ternary complexes in this model.
Error bars of simulated data are smaller than data points.
](svg/main_modeling_buffering.svg){width=5.999in}

\pagebreak

## Figure 4

![
**The human cytomegaloviral uORF2 buffers against reductions in main ORF translation.**  
The human cytomegaloviral *UL4* uORF2 is used in the dual-luciferase assay in conjunction with various mechanisms to reduce ribosome loading.
The no-stall uORF2 mutants lack their terminal diproline motifs (P22A mutation). Error bars show standard error of mean Nluc / Fluc ratios over 3 technical replicates.  
**(A)** Ribosome loading is reduced using stem-loops[@Babendure2006] with the indicated GC percentages.  
The -30 kcal/mol stem loops are positioned 8 bp from the 5\' cap.
<!-- Make sure that all are -30 kcal/mol even with varied GC % -->
The no-stem-loop data has a 5\' UTR CAA repeat instead of a stem-loop.
The data are vertically ordered by the no-stall means.
The 5\' UTR is 287 nt long.
Data are normalized to a no-uORF start codon control without a stem loop.  
**(B)** Ribosome loading is reduced using the drug 4ER1Cat (116 µM) that disrupts the interaction between eIF4E and eIF4G.  
Nanoluc has a C-terminal PEST tag to increase protein turnover for the 3-hour drug treatment[@Rechsteiner1996].
The 5\' UTR is 236 nt long.
Data are normalized to a no-uORF start codon control without a PEST tag.  
**(C)** Ribosome loading onto the uORF2-nanoluciferase portion of the transcript is reduced using a 5\' synthetic uORF.  
The synthetic uORF is comprised of several residues from the *GAPDH* ORF: ATG GGG TAG.  
The synthetic uORF Kozak is varied to tile ribosome loading.
The data are vertically ordered by the no-stall means.
The 5\' UTR is 262 nt long.
Data are normalized to a no-uORF start codon control without a synthetic uORF.
](svg/main_evidence_of_buffering_from_reduced_ribosome_loading.svg){width=5.379in}

\pagebreak

## Figure 5

![
**Changes to the distance between the human cytomegaloviral uORF2 start codon and elongation stall do not change repressiveness much as predicted by computational modeling of the collision-mediated 40S dissociation model.**  
**(A)** The distance between the human cytomegaloviral uORF2 start codon and elongation stall does not systematically affect its repression of main ORF translation.  
The human cytomegaloviral *UL4* uORF2 is used in the dual-luciferase assay in conjunction with various length inserts from the N-terminus of the *EYFP* main ORF.
The *EYFP* main ORF sequence is inserted directly 3\' to the uORF2 start codon.
The added sequence increases the distance between the uORF2 start codon and elongation stall.
The indicated mutations improve the uORF2 Kozak sequence, remove the start codon, and remove the elongation stall.
Error bars show standard error of mean NLuc / Fluc ratios over 3 technical replicates.
Data are normalized to a no-uORF start codon control.  
**(B)** Computational modeling predicts greater changes in uORF repressiveness with changes in the distance between the start codon and elongation stall in the queueing-mediated enhanced repression model.  
Parameters that best fit control data (Fig. [2](#figure-2)C, Table [1](#table-1)) are used here.
Data are normalized to a no-uORF start codon control.
Error bars of simulated data are smaller than data points.
](svg/main_effect_of_uorf_d_stall_on_repressiveness.svg){width=4.184in}

\pagebreak

## Figure 6

![
**Several human uORFs have repressive terminal diproline motifs.**  
Terminal diproline motif-containing human uORFs are used in the dual-luciferase assay.
Terminal proline residues are mutated to alanine residues in the P to A mutant.
Start codons are mutated to ACC for the no-AUG mutants.
P values comparing the indicated mutants to the wild-type are shown after running a two sample T-test: N.S. (P \> 0.05), \* (0.01 \< P \< 0.05), \*\* (0.001 \< P \< 0.01), **\*** (P \< 0.001).
All comparisons with no shown significances are N.S.
Data are normalized to a no-*UL4*-uORF2 start codon control.
](svg/main_human_uorfs.svg){width=2.861in}

\pagebreak

## Figure S1

![
**Modeling workflow.**  
**(A)** Molecules in the kinetic model.  
Molecules have components each of which have state values or bond partners.
For example, the mRNA (*M*) initiation footprint can either be *clear* of ribosomes, and therefore free to allow a *PIC~43S~* loading reaction, or *blocked* by a ribosome and unable to allow this reaction.  
**(B)** Reactions in the kinetic model.  
Explanation points and the following numbers indicate component interactions.
For example in the *PIC~43S~* loading reaction, the A-site (*a*) of the PIC binds to the mRNA (*M*) at codon 1 (the 5\' cap, *c~1~*).
These interactions create the molecule bindings indicated by open circles.
Plus signs between molecules indicates that they are not bound together.
](svg/supplemental_modeling_workflow.svg){width=5.941in}

\pagebreak

## Figure S2

![
**(A)** Buffering in the 80S-hit dissociation model is dependent on uORF length.  
uORF re-initiation is 0.2%.
uORF initiation is 80%.  
**(B)** The d~stall~ buffering dependency in the queuing-mediated enhanced repression model is relaxed with non-0 l~scan\ capture~.  
l~scan\ capture~ refers to the distance from a start codon from which a ribosome can initiate translation.
For d~stall~ values of 60, 63 nt, the uORF length is 21, 22 codons, respectively.  
**(C)** With an elongation stall, the 80S-hit dissociation model acquires d~stall~-dependent buffering similar to that in the queuing-mediated enhanced repression model (Fig. [3](#figure-3)C).  
uORF re-initiation is 0.2%.  
**(D)** Buffering in the 80S-hit dissociation model is greatly weakened with control matched parameters.  
Buffering in the 80S-hit dissociation model requires low re-initiation and is stronger with longer uORFs and higher dissociation rates; these requirements conflict with parameters (Table [1](#table-1)) obtained from matching modeling predictions (Fig. [2](#figure-2)D) to experimental control data (Fig. [2](#figure-2)C).
uORF initiation is 80%.
Buffering is absent or greatly weakened when the elongation stall is absent or present, respectively.
When the elongation stall is present, d~stall~ is 63 nt to prevent reduction to the queueing-mediated enhanced repression model.  
**(E)** Buffering in the regulated re-initiation model requires 2 uORFs.  
All rates and labels are identical to the main modeling figure unless otherwise specified.
Error bars of simulated data are smaller than data points.
](svg/supplemental_modeling_predictions.svg){width=5.745in}

\pagebreak

## Figure S3

![
**The human cytomegaloviral uORF2 d~stall~ does not strongly regulate the capacity of buffering against reductions in main ORF translation.**  
The human cytomegaloviral *UL4* uORF2 in the dual-luciferase assay. Ribosome loading is reduced with a 5\' synthetic uORF constructed from several residues of the *GAPDH* ORF: ATG GGG TAG.
The no-stall uORF2 mutants lack their terminal diproline motifs (P22A mutation).
No GAPDH start codon mutants (ATG to AAG) are depicted by transparent, gray bars with red Xs and have a higher relative ribosome loading rate onto the uORF2-Nluc portion of the transcript.
The distance between the uORF2 start codon and elongation stall is varied as indicated by adding 6 nt, GTC AGC, from the N-terminus of the *EYFP* main ORF.
Data are normalized to a no-uORF start codon control without a synthetic uORF.
](svg/supplemental_effect_of_d_stall_on_buffering.svg){width=3.7in}

\pagebreak

## Table 1

: Parameter ranges and control mutant fit values. Parameters used in modeling, some of which were varied to fit control mutant data Fig. [2](#figure-2)C.

| Parameter                                                | Value range                        | Control mutant fit value (80S-hit dissocation) | Control mutant fit value (queueing-mediated enhanced repression) | Control mutant fit value (collision-mediated 40S dissociation) | Reference                                        |
| -------------------------------------------------------- | ---------------------------------- | ------------------------------ | ------------------------------ | ------------------------------ | ------------------------------ |
| k~cap\ bind~ (s^-1^)                                     | 0.02-0.06                          | 0.016                                          | 0.023                                                            | 0.025                                                          |[@Yan2016; @Morisaki2016; @Wu2016]               |
| k~scan~ (residues/s)                                     | 1-10                               | 5                                              | 5                                                                | 5                                                              |[@Vassilenko2011; @Andreev2018]                  |
| k~start\ uORF2\ wild-type~ (s^-1^)                              | unknown                            | 0.1                                            | 0.5                                                              | 0.5                                                            | This work                                        |
| wild-type uORF initiation (%)                                   | unknown                            | 1.96                                           | 9.09                                                             | 9.09                                                           | This work                                        |
| k~start\ uORF2\ strong\ Kozak~ (s^-1^)                   | unknown                            | 20                                             | 5                                                                | 5                                                              | This work                                        |
| strong Kozak uORF initiation (%)                         | unknown                            | 80                                             | 50                                                               | 50                                                             | This work                                        |
| k~elong~ (residues/s)                                    | 3-10                               | 5                                              | 5                                                                | 5                                                              |[@Ingolia2011; @Yan2016; @Morisaki2016; @Wu2016] |
| k~elong\ stall~ (residues/s)                             | 0.001                              | 0.001                                          | 0.001                                                            | 0.001                                                          |[@Cao1998]                                       |
| k~terminate~ (s^-1^)                                     | 0.5-5                              | 1                                              | 1                                                                | 1                                                              |[@Ingolia2011]                                   |
| k~terminated\ ssu\ recycle\ uORF~ (s^-1^)                | unknown                            | 2                                              | 5                                                                | 5                                                              | This work                                        |
| uORF re-initiation (%)                                   | unknown                            | 71.4                                           | 50                                                               | 50                                                             | This work                                        |
| k~dissociate~ (s^-1^)                                    | unknown                            | 2                                              | 0                                                                | 2                                                              | This work                                        |
| uORF length (residues)                                   | 21                                 | 21                                             | 21                                                               | 21                                                             |[@Degnin1993]                                    |

\pagebreak

## Table S1

: List of plasmids used for this study

| Plasmid | Genotype | Figure | Source |
| ------- | -------- | ------ | ------ |
|pASHS64|	pGL3-gp48UTR-Nluc-Fluc|	Parent and 2|	Promega pGL3 into which gp48 5\' UTR-Nluc-Fluc was cloned (see methods) |
|pPNHS132|	pcmv-gfpdropout-nluc-pest-tsv40-ppgk1-fluc-t2a-hyg-tbgh|	Parent|	YTK090 via pPNHS126|
|pTBHS1|	pASHS64-uORF2-P22A|	2|	This work (exp1)|
|pTBHS2|	pASHS64-no-AUG-uORF2|	2|	This work (exp1)|
|pTBHS3|	pASHS64-cttaccatgg-uORF2|	2|	This work (exp1)|
|pTBHS12|	pASHS64-5\'-synthetic-uORF|	4|	This work (exp4)|
|pTBHS13|	pASHS64-5\'-synthetic-uORF-uORF2-P22A|	4|	This work (exp4)|
|pTBHS14|	pASHS64-uORF2-1-codon-longer|	5|	This work (exp5)|
|pTBHS15|	pASHS64-uORF2-2-codons-longer|	5|	This work (exp5)|
|pTBHS16|	pASHS64-uORF2-3-codons-longer|	5|	This work (exp5)|
|pTBHS17|	pASHS64-uORF2-4-codons-longer|	5|	This work (exp5)|
|pTBHS18|	pASHS64-stem-loop-GC52|	4|	This work (exp6)|
|pTBHS19|	pASHS64-stem-loop-GC62|	4|	This work (exp6)|
|pTBHS20|	pASHS64-stem-loop-GC78|	4|	This work (exp6)|
|pTBHS21|	pASHS64-stem-loop-GC92|	4|	This work (exp6)|
|pTBHS22|	pASHS64-no-stem-loop-CAA-repeat|	4|	This work (exp6)|
|pTBHS23|	pASHS64-5\'-synthetic-uORF-no-AUG|	4|	This work (exp4)|
|pTBHS24|	pASHS64-5\'-synthetic-uORF-no-AUG-uORF2-P22A|	4|	This work (exp4)|
|pTBHS25|	pASHS64-uORF2-7-codons-longer|	5|	This work (exp5)|
|pTBHS26|	pASHS64-uORF2-10-codons-longer|	5|	This work (exp5)|
|pTBHS35|	pASHS64-stem-loop-GC52-uORF2-P22A|	4|	This work (exp6)|
|pTBHS36|	pASHS64-stem-loop-GC62-uORF2-P22A|	4|	This work (exp6)|
|pTBHS37|	pASHS64-stem-loop-GC78-uORF2-P22A|	4|	This work (exp6)|
|pTBHS38|	pASHS64-stem-loop-GC92-uORF2-P22A|	4|	This work (exp6)|
|pTBHS39|	pASHS64-no-stem-loop-CAA-repeat-uORF2-P22A|	4|	This work (exp6)|
|pTBHS41|	pASHS64-actgtc-5\'-synthetic-uORF|	4|	This work (exp4)|
|pTBHS42|	pASHS64-cattgt-5\'-synthetic-uORF|	4|	This work (exp4)|
|pTBHS43|	pASHS64-gaatcg-5\'-synthetic-uORF|	4|	This work (exp4)|
|pTBHS44|	pASHS64-tactat-5\'-synthetic-uORF|	4|	This work (exp4)|
|pTBHS45|	pASHS64-tccaaa-5\'-synthetic-uORF|	4|	This work (exp4)|
|pTBHS46|	pASHS64-tttgaa-5\'-synthetic-uORF|	4|	This work (exp4)|
|pTBHS47|	pASHS64-actgtc-5\'-synthetic-uORF-uORF2-P22A|	4|	This work (exp4)|
|pTBHS48|	pASHS64-cattgt-5\'-synthetic-uORF-uORF2-P22A|	4|	This work (exp4)|
|pTBHS49|	pASHS64-gaatcg-5\'-synthetic-uORF-uORF2-P22A|	4|	This work (exp4)|
|pTBHS50|	pASHS64-tactat-5\'-synthetic-uORF-uORF2-P22A|	4|	This work (exp4)|
|pTBHS51|	pASHS64-tccaaa-5\'-synthetic-uORF-uORF2-P22A|	4|	This work (exp4)|
|pTBHS52|	pASHS64-tttgaa-5\'-synthetic-uORF-uORF2-P22A|	4|	This work (exp4)|
|pTBHS58|	pASHS64-5\'-synthetic-uORF-uORF2-2-codons-longer|	S3|	This work (exp4)|
|pTBHS59|	pASHS64-5\'-synthetic-uORF-uORF2-2-codons-longer-P22A|	S3|	This work (exp4)|
|pTBHS60|	pASHS64-5\'-synthetic-uORF-no-AUG-uORF2-2-codons-longer|	S3|	This work (exp4)|
|pTBHS61|	pASHS64-5\'-synthetic-uORF-no-AUG-uORF2-2-codons-longer-P22A|	S3|	This work (exp4)|
|pTBHS79|	pASHS64-C1orf43-uORF|	6|	This work (exp12)|
|pTBHS83|	pASHS64-TOR1AIP1-uORF|	6|	This work (exp12)|
|pTBHS84|	pASHS64-HAUS4-uORF|	6|	This work (exp12)|
|pTBHS86|	pASHS64-C15orf59-uORF|	6|	This work (exp12)|
|pTBHS87|	pASHS64-PPP1R37-uORF|	6|	This work (exp12)|
|pTBHS89|	pASHS64-ABCB9-uORF|	6|	This work (exp12)|
|pTBHS91|	pASHS64-C1orf43-uORF-P12A|	6|	This work (exp12)|
|pTBHS95|	pASHS64-TOR1AIP1-uORF-P25A|	6|	This work (exp12)|
|pTBHS98|	pASHS64-C15orf59-uORF-P24A|	6|	This work (exp12)|
|pTBHS99|	pASHS64-PPP1R37-uORF-P23A|	6|	This work (exp12)|
|pTBHS101|	pASHS64-ABCB9-uORF-P40A|	6|	This work (exp12)|
|pTBHS127|	pASHS64-C1orf43-no-AUG-uORF|	6|	This work (exp18)|
|pTBHS128|	pASHS64-C15orf59-no-AUG-uORF|	6|	This work (exp18)|
|pTBHS131|	pASHS64-ABCB9-no-AUG-uORF|	6|	This work (exp18)|
|pTBHS132|	pASHS64-PPP1R37-no-AUG-uORF|	6|	This work (exp18)|
|pTBHS133|	pASHS64-TOR1AIP1-no-AUG-uORF|	6|	This work (exp18)|
|pTBHS134|	pPNHS132-uORF2-Nluc-PEST|	4|	This work (exp15)|
|pTBHS135|	pPNHS132-uORF2-P22A-Nluc-PEST|	4|	This work (exp15)|

\pagebreak

## References
