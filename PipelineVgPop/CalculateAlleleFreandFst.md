After [SimulationToGfa.md](/SimulationToGfa.md). 

Now I calculate analysis of population genetics on GFA.

#### 1. Calculate Allele Frequencies on GFA

[GfatoAlleleFrequenciesMetadata.py](/GfatoAlleleFrequenciesMetadata.py)

For calculate AF I count ATGC in a position and I check the reference base and calculate for each allele the frequency (count/num_haplotype).

I had Allele Frequencies also as different of 1 and for triallelic sites I sumn frequencies of minimum allele.


#### 2. Calculate Genotype Frequencies on GFA
[GfatoGenotypeFrequencyMetadata.py] (/GfatoGenotypeFrequencyMetadata.py)

 
 #### 3. Calculate Fst on GFA
Two formules:
[GfatoFst.py](/GfatoFst.py)

 
