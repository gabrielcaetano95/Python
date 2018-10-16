#!/usr/bin/python3

Valor = 0

for x in range(0,10):
	N = int(input('(' + str(x+1) + ')' + 'Digite o valor: '))
	Valor = (Valor + N)
	print(round((Valor)/(x+1),2))