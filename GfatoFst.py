import statistics
import matplotlib.pyplot as pyplot

mean_fst_list = []

for num_rep in range(1,2):                                 #range replicate
	f1 = open('allelfr_rep{}.pop1.tsv'.format(num_rep))
	f2 = open('allelfr_rep{}.pop2.tsv'.format(num_rep))

fst_list = []
#f1.readline() # Skip header or first line
#f2.readline() 

for (line1, line2) in zip(f1, f2):
    freq_pop1 = line1.strip('\n').split('\t')[-1]   #last column
    freq_pop2 = line2.strip('\n').split('\t')[-1]  

    #print(freq_pop1)
    #print(freq_pop2)
    
    freq0_pop1 = float(freq_pop1)
    freq0_pop2=float(freq_pop2)
    mean = statistics.mean([freq0_pop1, freq0_pop2])
    #print(mean)

    fst = statistics.pvariance([freq0_pop1, freq0_pop2])/((mean)*(1-mean))
    #print(freq0_pop1, freq0_pop2)
    fst_list.append(fst)

    #f1.close()
    #f2.close()


    mean_fst_list.append(statistics.mean(fst_list))

print(mean_fst_list)
