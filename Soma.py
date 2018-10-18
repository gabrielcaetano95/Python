#!/usr/bin/python3

convidados = ['sergio','juliana','amanda']

try:
	pos = int(input('Digite posição do convidado: '))
	print(convidados[pos])

except ValueError:
	print('Apenas números')

except IndexError:
	print('A lista possui apenas ' + len(convidados) + ' convidados.')

except Exception as e:
	print(e)
	