## Thesis

### 1.GFAtoVCF and detection bubble: for validate results of pop analyses on GFA 

[GFAtoVCFodgi.py](GFAtoVCFodgi.py)

### 2. Simulation sequences (MS) to VCF and calculate Allele Frequencies and Fst on VCF for look if simulations works well. 

[ms2vcf.py](ms2vcf.py)

[CalculateFstonVCF.py](CalculateFstonVCF.py)

See: [SimulationToVcf.md](PipelineVgPop/SimulationToVcf.md)

### 3.Simulation sequences (MS) to GFA.
 
[MstoGfa.py](MstoGfa.py)  #don't use it.

### 4. SeqGen to GFA. 

With Seqgen I reconstruct ancestral sequence, because I have need 'links' between bubble.

[SeqgenToGfa.py](SeqgenToGfa.py)

See: [SimulationToGFA.md](PipelineVgPop/SimulationToGFA.md)

### 5. Metadata for info to individuals of pop1 and pop2.

 [Metadata.py](Metadata.py)

### 6. GFA to Allele Frequencies.

Allele Frequencies [GfatoAlleleFrequenciesMetadata.py](GfatoAlleleFrequenciesMetadata.py).

Genotyping Frequencies [GfatoGenotypeFrequenciesMetadata.py](GfatoGenotypeFrequenciesMetadata.py).

### 7. GFA to Fst: loading (two methods)

[GfatoFst.py](GfatoFst.py)

Fst interpopulation

Fst intrapopulation

See: [CalculateAlleleFr_FstonGfa.md](PipelineVgPop/CalculateAlleleFr_FstonGfa.md)

### 8. Allele frequencies on HLA


Author
Flavia Villani
