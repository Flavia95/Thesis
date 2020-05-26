from collections import Counter
path_node_id = {}
step_node_id = {}
pops_to_haplotypes_dict = {}
path_id_ref = ''
pop = ''

#Ragioniamo in termini di aplotipo,Calculate Allele Frequencies

#1. Load metadata for calculate info of tree leaves and dict (key:num_pop and value:num_haplo)
with open('metadata280pop.tsv', 'r') as f:
    f.readline()
    for line in f:                                              #'1'(pop): ['1', '2'],
                                                                #'2'(pop): ['3', '4']
        num_pop, num_haplo = line.strip('\n').split('\t')
        if num_pop not in pops_to_haplotypes_dict.keys():
            pops_to_haplotypes_dict[num_pop] = []
        pops_to_haplotypes_dict[num_pop].append(num_haplo)
    #print(pops_to_haplotypes_dict)

#2. Load rep {range} fromSeqgeneToGfa and mantain info of pathid and stepid(from line that start with Path) and id and seq(from line that start with Seq)

for num_rep in range(3, 4):
    print('Num. replicate: ', num_rep)
    
    with open("rep{}.seq.gfa".format(num_rep),"r") as f:
        for line in f:
            line_list = line.strip('\t').split('\t') 
            if line.startswith('P'):
                path_node_id[line_list[1]] = [x.strip('+') for x in line_list[2].strip('\n').split(',')]   #pathid and stepid
                
                if 'ref' in line_list[1].lower():
                    path_id_ref = line_list[1]
            elif line.startswith('S'):
                step_node_id[line_list[1]] = line_list[2].strip('\n')    #id and seq  

   
#3.Info for num of populations    
    for num_pop, individual_haplotypes_list in pops_to_haplotypes_dict.items():
        to_write = ''
        pop = ('Population num.', num_pop)
        print(pop)

        num_haplotypes = len(individual_haplotypes_list)

        for pos in range(len(path_node_id[path_id_ref])):
            tmp_seq_in_pos_list = []
            
            for path_id, step_id_list in path_node_id.items():
                if path_id in individual_haplotypes_list:
                    
                    seq_current_step = step_node_id[step_id_list[pos]]
                    #print('\t' + path_id, seq_current_step)
                    tmp_seq_in_pos_list.append(seq_current_step)

            triall_dict = {}
            #print('\tPos', pos, '- sequences in this pos', tmp_seq_in_pos_list)
            ATCG_counts_dict = Counter(tmp_seq_in_pos_list)
            #print('\tPos', pos, '- ', ATCG_counts_dict)   #I put delete it, is not necessary
            

            for nucleotide, count in ATCG_counts_dict.items():
                if count/num_haplotypes != 1:
                    #print(str(pos) + '\t'+ str(nucleotide)+ '\t'+ str(count/num_haplotypes))  #printa anche i triallelici questo
                           
                    
                        if len(str(pos)) >=1 not in triall_dict.keys():    #delete this
                            triall_dict[pos] = []                          
                           
#4. If triallelic sites, sumn minor allele frequencies                          
            if len(ATCG_counts_dict) > 1:     
                if len(ATCG_counts_dict) > 2:
                    print(ATCG_counts_dict, max(ATCG_counts_dict, key=ATCG_counts_dict.get))
                    new_dict = {}
                    nt_min_count = 'X' #min(ATCG_counts_dict, key=ATCG_counts_dict.get)
                    nt_max_count = max(ATCG_counts_dict, key=ATCG_counts_dict.get)
                    for nt, count in ATCG_counts_dict.items():
                        if nt == nt_max_count:
                            new_dict[nt] = count
                        else:
                            if nt_min_count not in new_dict:
                                new_dict[nt_min_count] = 0
                            new_dict[nt_min_count] += count

                    ATCG_counts_dict = new_dict
                
#5. Write file tsv that contains genotype frequencies for each population and write two file, one for population                              
                for nucleotide, count in ATCG_counts_dict.items():
                    fr_allel = ('\t'.join([str(pos) + '\t'+ str(nucleotide)+ '\t'+ str(count/num_haplotypes)]) + '\n')
                    print(fr_allel.strip('\n'))
                    to_write += fr_allel


        with open('allelfr_rep{}.pop{}.tsv'.format(num_rep, num_pop), 'w') as fw:
            fw.write(to_write)
