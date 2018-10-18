#!/usr/bin/python3

convidados = ['sergio','juliana','amanda']

try:
	pos = int(input('Digite posição do convidado: '))
	print(convidados[pos])

except TypeError:
	print('Apenas números')

except IndexError:
	print('A lista possui apenas ' + str(len(convidados)) + ' convidados.')

except Exception as e:
	print(e)
