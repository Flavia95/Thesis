import os

ms_command = ''

with open('/home/flavia/Desktop/GfatoAlleleFreq/tree2pop.ms','r') as f:
	ms_command = f.readline().strip('\n')

print('ms_command: '+ ms_command)     

if '-I' in ms_command:
	info_list = ms_command.split('-I ')[1].split(' ')[:3]   #extract individual and pop from ms command (I)
	print('-I list:', info_list)

	POP = int(info_list[0])
	NumHaplo = int(info_list[1])
	ind = int(info_list[2])
	
	#for indiv in range (1, (NumHaplo + ind)+1):
		#print('-individual',indiv)
	

	metadata = ' '
		

	for pop in range(1, POP+1):
		for haplo in range(1,NumHaplo+1):
			metadata = ('POP',pop,'individual:', int((haplo - 1) / 2), 'haplo', haplo) 
			print(metadata)


			#TODO: add version of script that there is write of a file metadata tab separated

			
'''
metadata = 'metadata' 
with open(metadata, 'w') as fw:
    fw.write(str(paths_to_write))
    print(metadata + ' written')
'''