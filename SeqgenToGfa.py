ref_seq = ''
                                                                 #for more replicates
path_input = 'T1.seqgen'             #Input:2popwith40seqforpop100rep

with open(path_input) as f:
    for num_rep, i in enumerate(f.read().split('\n ')):   #with for I read single file and with external loop read and split output in N replicate
        ref_seq = ''

        seq_list = i.strip(' \n').split('\n')
        num_ref, len_seq = seq_list[0].split(' ')
        num_ref = int(num_ref) + 1
        seq_list = seq_list[2:]

        for num, seq in [x.split('\t') for x in seq_list]:
            if int(num) == num_ref:
                ref_seq = seq
                break

        #print(num_ref, len_seq, seq_list)

        if ref_seq == '':
            print('No reference found!')
            continue


        # The first step_id is the reference step id
        pos_to_step_ids_in_that_pos_dict = {}
            
        step_id_to_seq_dict = {}
        path_to_nodes_dict = {} # Name and Step List
        path_nodes_dict = {}

        links_to_write = ''  #for write output, define links, steps and paths
        steps_to_write = ''
        paths_to_write = ''


        path_nodes_dict['AncestralReference'] = []
        for step_id, nt in enumerate(ref_seq):
            step_id_to_seq_dict[step_id] = nt
            
            path_nodes_dict['AncestralReference'].append(str(step_id))
            
            pos_to_step_ids_in_that_pos_dict[step_id] = [step_id]
            
        last_step_id = step_id + 1

        stuff_already_seen = set()
        for num, seq in [x.split('\t') for x in seq_list]:
            # If it is not the reference...
            if int(num) != num_ref:
                # ...find differences
                
                path_nodes_dict[num] = []
                last_chosen_node = -1
                for pos, (x, y) in enumerate(zip(ref_seq, seq)):
                    choosen_step_id = -1
                    if x == y:
                        choosen_step_id = pos_to_step_ids_in_that_pos_dict[pos][0] # The first step id is the reference step id
                    else:
                        for possible_step_id in pos_to_step_ids_in_that_pos_dict[pos]:
                            if step_id_to_seq_dict[possible_step_id] == y:
                                # Already available a node with the same sequence
                                choosen_step_id = possible_step_id
                                break
                        
                        if choosen_step_id == -1:
                            # I need to create a new step_id
                            step_id_to_seq_dict[last_step_id] = y
                            pos_to_step_ids_in_that_pos_dict[pos].append(last_step_id)
                            choosen_step_id = last_step_id
                        
                            last_step_id += 1
                    path_nodes_dict[num].append(str(choosen_step_id))
                    
                    # Links
                    if last_chosen_node != -1:
                        nodo_1 = last_chosen_node
                        nodo_2 = choosen_step_id
                        nodo_12 = str(nodo_1) + '_' + str(nodo_2)
                        if nodo_12 not in stuff_already_seen:
                            stuff_already_seen.add(nodo_12)
                            links_to_write += 'L\t' + str(nodo_1) + '\t+\t' + str(nodo_2) + '\t+\t0M\n'
                            
                    last_chosen_node = choosen_step_id
                    

                        
        for step_id, seq in step_id_to_seq_dict.items():
            #print('\t'.join(['S', str(step_id), seq]))
            steps_to_write += 'S\t'+ str(step_id) + '\t' + seq + '\n'
            

        for path, node_list in path_nodes_dict.items():
            paths_to_write += ('\t'.join(['P', path,'+,'.join(node_list) + '+', '\n']))

            

        path_gfa = 'rep{}.seqtogfaT1.gfa'.format(num_rep)
        with open(path_gfa, 'w') as fw:
            fw.write(steps_to_write + paths_to_write + links_to_write)
        print(path_gfa + ' written')

