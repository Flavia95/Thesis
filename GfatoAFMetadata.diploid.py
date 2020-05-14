from collections import Counter


path_node_id = {}
step_node_id = {}

path_id_ref = ''

# IMPLEMENTAZIONE SEMPLIFICATA: RAGIONIAMO IN TERMINI DI APLOTIPO, SENZA
# RAGGRUPPARE GLI APLOTIPI A 2 A 2 (se gli individui sono diploidi)    qui prendere 2 aplo
pops_to_haplotypes_dict = {}
with open('metadata280pop.tsv', 'r') as f:
    f.readline()

    for line in f:
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

    triall_dict = {}

    num_diploid_individuals = len(individual_haplotypes_list) / 2

    for pos in range(len(path_node_id[path_id_ref])):
        tmp_seq_in_pos_list = []
        
        it = iter(individual_haplotypes_list)
        for path_id_haplo_1 in it:
            path_id_haplo_2 = next(it)

            seq_current_step = step_node_id[path_node_id[path_id_haplo_1][pos]] + step_node_id[path_node_id[path_id_haplo_2][pos]]
            #print('\t' + path_id_haplo_1, path_id_haplo_2, seq_current_step)
            tmp_seq_in_pos_list.append(seq_current_step)

        #print('\tPos', pos, '- sequences in this pos', tmp_seq_in_pos_list)
        ATCG_counts_dict = Counter(tmp_seq_in_pos_list)
        #print('\tPos', pos, '- ', ATCG_counts_dict)   #I put delete it, is not necessary

        for nt_nt, count in ATCG_counts_dict.items():
            if count/num_diploid_individuals != 1:
                if pos not in triall_dict.keys():
                    triall_dict[pos] = {}
                triall_dict[pos][nt_nt] = count/num_diploid_individuals                       


    with open('gfa_fralle_pop' + str(num_pop) + '.tsv', 'w') as fw:
        for pos, nt_nt_freq_dict in triall_dict.items():
            for nt_nt, freq in nt_nt_freq_dict.items():
                fw.write(str(pos) + '\t' + nt_nt + '\t' + str(freq) + '\n')
