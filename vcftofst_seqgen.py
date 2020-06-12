import statistics
import matplotlib.pyplot as plt

mean_fst_list = []

for T in ['1', '2', '3']:
	for num_rep in range(0,99):                               #usare con tanti replicati
	    #print('Num. rep:', num_rep)
	    f1 = open('t{}/vcf/seqgen.rep{}.T{}.bcf.pop1.vcf.frq'.format(T, num_rep, T))    #formulaFst: deviazione/media(1-media)
	    f2 = open('t{}/vcf/seqgen.rep{}.T{}.bcf.pop2.vcf.frq'.format(T, num_rep, T))

	    fst_list = []
	    f1.readline() # Skip header
	    f2.readline() # Skip header
	    for (line1, line2) in zip(f1, f2):
	        freq_pop1_list = line1.strip('\n').split('\t')[4:]
	        freq_pop1_list = [
	            float(x.split(':')[1]) for x in freq_pop1_list if (float(x.split(':')[1]) != 0) and (float(x.split(':')[1]) != 1)
	        ]
	        freq_pop2_list = line2.strip('\n').split('\t')[4:]
	        freq_pop2_list = [
	            float(x.split(':')[1]) for x in freq_pop2_list if (float(x.split(':')[1]) != 0) and (float(x.split(':')[1]) != 1)
	        ]
	        if len(freq_pop1_list) != 2 or len(freq_pop2_list) != 2:
	            #print('Not biallelic site')
	            continue
	        
	        freq0_pop1 = sorted(freq_pop1_list)[0]
	        freq0_pop2 = sorted(freq_pop2_list)[0]

	        mean = statistics.mean([freq0_pop1, freq0_pop2])
	        fst = statistics.pvariance([freq0_pop1, freq0_pop2])/((mean)*(1-mean))
	        
	        #print(mean)
	        #print(line1.strip('\n'))
	        #print(line2.strip('\n'))
	        #   print(freq0_pop1, freq0_pop2)
	        fst_list.append(fst)
	    
	    f1.close()
	    f2.close()

	    if len(fst_list) == 0:
	        #print('Missing variants rep:', num_rep)
	        continue


	    mean_fst_list.append(statistics.mean(fst_list))

	print('t{} <- c({})'.format(T, ','.join([str(x) for x in mean_fst_list])))
	#print(len(mean_fst_list))
