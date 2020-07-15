![sPLinter](logo.png) <!-- .element height="50%" width="50%" --> 

<!-- .element <u>S</u>tructural <u>P</u>rotein <u>L</u>igand <u>Inter</u>action Descriptors -->

# What are protein-ligand interaction descriptors ?
Protein-ligand complexes are formed mainly by reversible non-covalent interaction between the protein and ligand molecules. The interaction is a combination of hydrogen bonds, hydrophobic forces, van der Waals forces, pi-pi interactions and electrostatic interactions in which there is no sharing of electrons between the two interacting partner molecules. The binding affinity of protein ligand can be described by a comphrehensive representation of these interactions, called interaction descriptors, which provide information on the interaction partners, the structural and sequence context of the interaction and a quantitative description of the strength of the interaction.

# What's the problem?
Analysis of protein-ligand interactions is critical to understand how endogenous ligands bind and how potential drug molecules can bind to orthosteric and allosteric binding sites in proteins. Membrane proteins like receptors present multiple allosteric sites, which can be rationally targeted by new drugs as these sites are less conserved than the orthosteric sites.
Evaluation of binding affinity of the protein with ligand is the primary focus in the rational drug-design or to understand structure-function relationships. The binding affinity is determined by a combination of all types of moleclar interactions. In addition the binding affinity is influenced by the environmental variables such as pH, temperature, ionic concentrations etc of the medium. Having a comphrehensive and computationally usable format of the interactions is thus essential for other analytical modules and graphical representation features of iCN3D.

# What is sPLinter ?

sPLinter is a code module that extracts protein-ligand interactions which can be plugged into other computational modules of iCN3D. 
Its Goal is to combine detailed information on ligand binding residues in proteins (in terms of biochemical interactions like salt-bridge, hydrogen bonding, pi-pi interactions, water-mediated interactions, etc.) with sequence/structure conservation analysis of the binding sites in related proteins, one can devise a rational strategy for drug design.

# Installation 
TBD

## Dependencies
TBD
### Python modules
json,pandas,xml
### Protein-Ligand Interaction Profiler (https://projects.biotec.tu-dresden.de/plip-web/plip/index)
For identification of noncovalent interactions between proteins and their ligands.
### ACPYPE (https://pypi.org/project/acpype/)
For topology file generation
### Amber-tools20 (http://ambermd.org/AmberTools.php)
For interaction energy computation
### GROMACS (http://www.gromacs.org/) or NAMD (https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=NAMD)
To setup the molecule for energy calculation

  
# Configuration
TBD
  
# Usage
TBD
## Generate PLIP interactions

## Create interaction list

### The xmlToJSON.py get a xml from Protein-Ligand Interaction Profiler (PLIP) database and provide a JSON file.

To run the script in the shell you can use the following command line: <br>
> ./xmlToJSON.py -x plipFile.xml

For further information: <br>
> ./xmlToJSON.py -h

### Compare interactions for two ligands at the same residues: MultiIndexing: Interaction specific

> xmlToJSON.py -j1 <jsonfile1> -j2 <jsonfile2> -o <outputCsv> <br>
-j1 --jsonfile1:	First JSON file obtained by xmlToJSON.py script <br>
-j2 --jsonfile2:	Second JSON file obtained by xmlToJSON.py script <br>
-o --outputCsv:	CSV output file
  
## Pre-process protein complex and calculate energies

## Create interaction list with energies


# Testing
TBD

# Citing
TBD

# Contact
abrol@csun.edu Ravi Abrol <br>
ayllonbenitez.aaron@gmail.com	Aaron Ayllon-Benitez <br>
sangramsahu15@gmail.com	Sangram Keshari Sahu <br>
rachita.kumar9@gmail.com	Rachita K Kumar <br>
sreeranjinibabu611@gmail.com	Sreeranjini Babu <br>
smalkaram@wvstateu.edu	Sridhar Acharya Malkaram


