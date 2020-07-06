import statistics
#import matplotlib.pyplot as plt
import numpy as np
for T in ['1', '2', '3']:
    mean_fst_list = []
    for num_rep in range(0,99):                               #usare con tanti replicati
        f1 = open('t{}/seqgen.rep{}.bial.vcf.pop1_pop2.weir.fst'.format(T, num_rep))   
        

        f1.readline()
        fst_list = []

        #pos_set = set()
        #pos_to_freq_pop1 = {}
        for line1 in f1:
            fst = line1.strip('\n').split('\t')[-1]
            if 'nan' not in fst:
                fst_list.append(float(fst))



        f1.close()


        mean = statistics.mean(fst_list)
        mean_fst_list.append(mean)


    print('t{} <- c({})'.format(T, ','.join([str(x) for x in mean_fst_list])))    