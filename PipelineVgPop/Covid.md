Pipeline assembly de novo

1. seqtk seq -a ERX4112805.fastq > ERX4112805.fasta #convert fastq in fasta

2. /home/flavia/tools/minimap2 -c NC_045512.2.fasta ERX4112805.fasta > ERX4112805.paf
#mapvsref

3. ./seqwish -s <(cat /home/flavia/Desktop/recover/NC_045512.2.fasta /home/flavia/Desktop/recover/ERX4112805.fasta) -p /home/flavia/Desktop/recover/ERX4112805.paf -g /home/flavia/Desktop/recover/ERX4112805.gfa  #come se fosse un |

4. ./smoothxg -a --gfa-in /home/flavia/Desktop/recover/ERX4112805.gfa > /home/flavia/Desktop/recover/ERX4112805.smooth

a. prendere solo path che hanno consensus sotto forma di fasta

grep -v ^P > withoutP
grep 'Consensus_' ERX4112805.smooth > senzapath
cat senzapath withoutP > ERX4112805smoothwithpath.gfa

6. convertire gfa in fasta

./odgi paths -i /home/flavia/Desktop/recover/ERX4112805.smoothoutpath.og -f > /home/flavia/Desktop/recover/ERX4112805.smoothoutpathog.fasta


7. /home/flavia/tools/minimap2 NC_045512.2.fasta ERX4112805.smoothoutpathog.fasta > refvsERx4112805.paf

a. dotplotly

