Pipeline

1. seqtk seq -a ERX4112805.fastq > ERX4112805.fasta #convert fastq in fasta

2. /home/flavia/tools/minimap2 NC_045512.2.fasta ERX4112805.fasta > ERX4112805.paf
#mapvsref

3. ./seqwish -s /home/flavia/Desktop/recover/ERX4112805.fasta -p /home/flavia/Desktop/recover/ERX4112805.paf -g /home/flavia/Desktop/recover/ERX4112805.gfa

#induce graph

4. ./smoothxg -a --gfa-in /home/flavia/Desktop/recover/ERX4112805.gfa > /home/flavia/Desktop/recover/ERX4112805.smooth
