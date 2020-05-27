After [SimulationToGFA.md](SimulationToGFA.md) where I convert MStoGfa for analysis of population genetics.
 
#### 1. Extract individuals from one or two populations

[Metadata.py](/Metadata.py)

 #### 2. Calculate Allele Frequency on GFA :)

For calculate AF I count ATGC in a position and I check the reference base and calculate for each allele the frequency (count/num_haplotype).
 
 [GfatoAlleleFrequenciesMetadata.py](/GfatoAlleleFrequenciesMetadata.py)
 
 #### 3. Calculate Genotype Frequency on GFA
 
 [GfatoGenotypeFrequenciesMetadata.py](/GfatoGenotypeFrequenciesMetadata.py)
 
 #### 4. Calculate Fst on GFA
[GfatoFst.py](/GfatoFst.py)
 
 
