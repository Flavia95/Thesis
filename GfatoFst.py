import statistics
import matplotlib.pyplot as pyplot
mean_fst_list = []
fst_list = []

#1. Calculate Fst = variance/(mean)*(1-mean)
#Open files of allele_freq from pop1 and allele_freq from pop2

for num_rep in range(0,98):                               
    f1 = open('allelfr_rep{}.pop1.tsv'.format(num_rep))    
    f2 = open('allelfr_rep{}.pop2.tsv'.format(num_rep))

    for (line1, line2) in zip(f1, f2):
        freq_pop1 = line1.strip('\n').split('\t')[-1]   #last column for allel_freq
        freq_pop2 = line2.strip('\n').split('\t')[-1]  
	#print(freq_pop1)
        #print(freq_pop2)
        
#2.Mean of frequencies	
	freq0_pop1 = float(freq_pop1)
        freq0_pop2=float(freq_pop2)
        mean = statistics.mean([freq0_pop1, freq0_pop2])
        #print(mean)

#3.Calculate Fst
        fst = statistics.pvariance([freq0_pop1, freq0_pop2])/((mean)*(1-mean))
        #print(freq0_pop1, freq0_pop2)
        
	fst_list.append(fst)
	
if len(fst_list) == 0:
   print(num_rep, 'missing values', fst_list)
   continue

    mean_fst_list.append(statistics.mean(fst_list))

    f1.close()
    f2.close()

print(mean_fst_list)
print(len(mean_fst_list))
