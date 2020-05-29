import os
import sys

ms_command = ''

with open('treems400popT1','r') as f:
	ms_command = f.readline().strip('\n')
	   
print('ms_command: '+ ms_command)     

if '-I' not in ms_command:                         
	print('The -I option is missing')
	sys.exit(-1)

info_list = [int(x) for x in ms_command.split('-I ')[1].split(' -')[0].split(' ')]     #extract individual and pop from ms command (I)
print('-I list:', info_list)                                                           #-I: first is the num of pop, two is the seq of pop1 and three the seq of pop2

num_subpop = info_list[0]
num_haplo_for_each_subpop_list = info_list[1:]

if num_subpop != len(num_haplo_for_each_subpop_list):
	print('Num. subpopulations is different from the number of sample configurations')
	sys.exit(-2)

print('Num. subpopulations:', num_subpop)
print('Sample configurations:', num_haplo_for_each_subpop_list)


num_current_haplo = 1
with open('metadata2pop400.tsv', 'w') as fw:                                              
	fw.write('\t'.join(['NumSubPopulation', 'NumHaplotype']) + '\n')                             #write info for next analyses,NumHaplotype
	for num_subpop, num_haplo_subpop in enumerate(num_haplo_for_each_subpop_list):
		for _ in range(1, num_haplo_subpop + 1):
			fw.write('\t'.join([str(num_subpop + 1),str(num_current_haplo)]) + '\n')

			num_current_haplo += 1
