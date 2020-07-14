![sPLinter](logo.png?raw=true "Title" width="200" height="400")

# What are protein-ligand interaction descriptors ?
Protein-ligand complexes are formed mainly by reversible non-covalent interaction between the protein and ligand molecules. The interaction is a combination of hydrogen bonds, hydrophobic forces, van der Waals forces, pi-pi interactions and electrostatic interactions in which there is no sharing of electrons between the two interacting partner molecules. The binding affinity of protein ligand can be described by a comphrehensive representation of these interactions, called interaction descriptors, which provide information on the interaction partners, the structural and sequence context of the interaction and a quantitative description of the strength of the interaction.

# What's the problem?
Analysis of protein-ligand interactions is critical to understand how endogenous ligands bind and how potential drug molecules can bind to orthosteric and allosteric binding sites in proteins. Membrane proteins like receptors present multiple allosteric sites, which can be rationally targeted by new drugs as these sites are less conserved than the orthosteric sites.
Evaluation of binding affinity of the protein with ligand is the primary focus in the rational drug-design or to understand structure-function relationships. The binding affinity is determined by a combination of all types of moleclar interactions. In addition the binding affinity is influenced by the environmental variables such as pH, temperature, ionic concentrations etc of the medium. Having a comphrehensive and computationally usable format of the interactions is thus essential for other analytical modules and graphical representation features of iCN3D.

# What is sPLinter ?

sPLinter is a code module that extracts protein-ligand interactions which can be plugged into other computational modules of iCN3D. 
Its Goal is to combine detailed information on ligand binding residues in proteins (in terms of biochemical interactions like salt-bridge, hydrogen bonding, pi-pi interactions, water-mediated interactions, etc.) with sequence/structure conservation analysis of the binding sites in related proteins, one can devise a rational strategy for drug design.
