import statistics
#import matplotlib.pyplot as plt

mean_fst_list = []

for T in ['1', '2', '3']:
    for num_rep in range(0,99):                               #usare con tanti replicati
        #print('Num. rep: ', num_rep)
        f1 = open('t{}/allelfr_rep{}.pop1.tsv'.format(T, num_rep))    #formulaFst: deviazione/media(1-media)
        f2 = open('t{}/allelfr_rep{}.pop2.tsv'.format(T, num_rep))

        fst_list = []
        #f1.readline() # Skip header
        #f2.readline() # Skip header

        pos_set = set()
        pos_to_freq_pop1 = {}
        for line1 in f1:
            pos_pop1 = int(line1.strip('\n').split('\t')[0])
            lecter1 = line1.strip('\n').split('\t')[1]
            freq_pop1 = line1.strip('\n').split('\t')[-1]   #ultima colonna 
            
            if lecter1 == 'X' or freq_pop1 == 0 or freq_pop1 == 1:
                continue

            if pos_pop1 not in pos_to_freq_pop1:
                pos_to_freq_pop1[pos_pop1] = []
            pos_to_freq_pop1[pos_pop1].append(float(freq_pop1))

            pos_set.add(pos_pop1)

        pos_to_freq_pop2 = {}
        for line2 in f2:
            pos_pop2 = int(line2.strip('\n').split('\t')[0])
            lecter2 = line2.strip('\n').split('\t')[1]
            freq_pop2 = line2.strip('\n').split('\t')[-1]  #ultima colonna

            if lecter2 == 'X' or freq_pop2 == 0 or freq_pop2 == 1:
                continue

            if pos_pop2 not in pos_to_freq_pop2:
                pos_to_freq_pop2[pos_pop2] = []
            pos_to_freq_pop2[pos_pop2].append(float(freq_pop2))

            pos_set.add(pos_pop2)
        f1.close()
        f2.close()

        for pos in sorted(pos_set):
            if pos in pos_to_freq_pop1 and pos in pos_to_freq_pop2:
                if len(pos_to_freq_pop1[pos]) != 2 or len(pos_to_freq_pop2[pos]) != 2:
                    #print('Not biallelic site')
                    continue
                #print('pop1', pos, pos_to_freq_pop1[pos])
                #print('pop2', pos, pos_to_freq_pop2[pos])
                #print(freq_pop1)
                #print(freq_pop2)
                freq_pop1 = sorted(pos_to_freq_pop1[pos])[0]
                freq_pop2 = sorted(pos_to_freq_pop2[pos])[0]


                mean = statistics.mean([freq_pop1, freq_pop2])
                #print(mean)

                fst = statistics.pvariance([freq_pop1, freq_pop2])/((mean)*(1-mean))
                #print(freq_pop1, freq_pop2)
                
                fst_list.append(fst)

        if len(fst_list) == 0:
            #print(num_rep, 'missing values', fst_list)
            continue

        mean_fst_list.append(statistics.mean(fst_list))

    print('t{} <- c({})'.format(T, ','.join([str(x) for x in mean_fst_list])))
    #print(len(mean_fst_list))
