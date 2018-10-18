#!/usr/bin/python3

nomes = ['joao','maria','jose','paulo','isabela']

s = input('buscar por nome: ')

for nome in nomes:
	if s == nome:
		print('está na lista')
		break

else:
	print('Não está na lista')

