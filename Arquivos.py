#!/usr/bin/python3

nomes = ['yasmin','rafael','jessica']

with open('lista','w') as a:
	for nome in nomes:
		a.write(nome + '\n')
	#a.write(x, sep = '\n')




# try:
# 	with open('nome','x') as f:
# 		f.write('\tolá\n')

# except FileExistsError as e:
# 	with open('nome2','w') as f:
# 		f.write('\tolá\n\toi\n{}\n'.format(e))


# f = open('teste.txt','w')
# f.write('curso python')
# f.close()

# with open('log','r') as f:
# 	print(f.read())
# 	b = f.readlines()
# 	print(b[0] + b[3] + b[6] + '\n')