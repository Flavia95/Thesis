from collections import Counter

path_node_id = {}
step_node_id = {}

path_id_ref = ''

# IMPLEMENTAZIONE SEMPLIFICATA: RAGIONIAMO IN TERMINI DI APLOTIPO, SENZA
# RAGGRUPPARE GLI APLOTIPI A 2 A 2 (aggiungere script aggiornato, come fare con i genotipi?)
pops_to_haplotypes_dict = {}
with open('metadata280pop.tsv', 'r') as f:
    f.readline()
    for line in f:                                              #'1'(pop): ['1', '2'],
                                                                #'2'(pop): ['3', '4']
        num_pop, num_haplo = line.strip('\n').split('\t')
        if num_pop not in pops_to_haplotypes_dict.keys():
            pops_to_haplotypes_dict[num_pop] = []
        pops_to_haplotypes_dict[num_pop].append(num_haplo)
    #print(pops_to_haplotypes_dict)

with open("rep3.seq.gfa","r") as f:
    for line in f:
        line_list = line.strip('\t').split('\t') 
        if line.startswith('P'):
            path_node_id[line_list[1]] = [x.strip('+') for x in line_list[2].strip('\n').split(',')]   #pathid and stepid
            
            if 'ref' in line_list[1].lower():
                path_id_ref = line_list[1]
        elif line.startswith('S'):
            step_node_id[line_list[1]] = line_list[2].strip('\n')    #id and seq  


for num_pop, individual_haplotypes_list in pops_to_haplotypes_dict.items():
    print('Population num.', num_pop)

    num_haplotypes = len(individual_haplotypes_list)

    for pos in range(len(path_node_id[path_id_ref])):
        tmp_seq_in_pos_list = []
        
        for path_id, step_id_list in path_node_id.items():
            if path_id in individual_haplotypes_list:
                
                seq_current_step = step_node_id[step_id_list[pos]]
                #print('\t' + path_id, seq_current_step)
                tmp_seq_in_pos_list.append(seq_current_step)


        #print('\tPos', pos, '- sequences in this pos', tmp_seq_in_pos_list)
        ATCG_counts_dict = Counter(tmp_seq_in_pos_list)
        print('\tPos', pos, '- ', ATCG_counts_dict)   #I put delete it, is not necessary

        for nucleotide, count in ATCG_counts_dict.items():
            if count/num_haplotypes != 1:
                print('\t\tPos', pos, nucleotide, count/num_haplotypes)  #todo: put it in a file
