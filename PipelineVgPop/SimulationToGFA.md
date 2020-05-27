After [SimulationToVcf.md](SimulationToVcf.md). 

Now I convert MStoGfa for analysis of population genetics.

I simulated two populations that are divided into three different times.

#### 1. MS to GFA
 
[MstoGfa.py](/MstoGfa.py)

I get the GFA but I need the whole sequence rebuilt and the links between the bubbles for use "odgi".

#### 2. Reconstruct sequence 

```
./ms 4 1 -T -t 11.2 -I 2 2 2 -g 1 44.36 -n 2 0.05 -eg 0.03125 1 0.0 -ej 0.03125 2 1 > tree.ms 
```
I have Tree with the family history, but the reconstructed sequence is missing.
 
 ```
 seq-gen -mHKY -l 40 -s .2 -wa -z 783763255346462154 <tree.ms> seqwa.seqgen
```
```
 seq-gen -mHKY -l 40 -s .2 -z 783763255346462154 <tree.ms> seq.seqgen
```
 I use -z for set no random seed to try even without wa. 
 
 I get the same result, but -wa write Ancestral Sequences that was not in the tree of ms.
 
 #### 3. Seq-gene to GFA
 Simulation for three different time

```
./ms 80 100 -T -t 11.2 -I 2 40 40 -g 1 44.36 -n 2 0.05 -eg 0.03125 1 0.0 -ej 0.03125 2 1 > treems40popT1  #5.000 generazioni
```
```
./ms 80 100 -T -t 11.2 -I 2 40 40 -g 1 44.36 -n 2 0.05 -eg 0.03125 1 0.0 -ej 0.0625 2 1 > treems40popT2  #10.000 generazioni
```
```
./ms 80 100 -T -t 11.2 -I 2 40 40 -g 1 44.36 -n 2 0.05 -eg 0.03125 1 0.0 -ej 0.09375 2 1 > treems40popT3  #15.000 generazioni 
```
Reconstruct sequence for three different time

```
seq-gen -mHKY -l 40 -s .2 -wa -z 783763255346462154 <treems40popT1> T1.seqgen
 ```
 ```
seq-gen -mHKY -l 40 -s .2 -wa -z 783763255346462154 <treems40popT2> T2.seqgen
 ```
 ```
seq-gen -mHKY -l 40 -s .2 -wa -z 783763255346462154 <treems40popT3> T3.seqgen
 ```

I convert SeqGen to Gfa

[SeqgentoGfa.py](/SeqgenToGfa.py)

I calculate on GFA Allele Frequencies, Genotype Frequencies and Fst.
[CalculateAlleleFr_FstonGfa.md](CalculateAlleleFr_FstonGfa.md)
 
 
