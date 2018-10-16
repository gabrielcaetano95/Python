#!/usr/bin/python3

n = ['a','e','i','o','u','A','E','I','O','U']
valor = 0

palavra = str(input('Digite o texto: '))

for x in palavra:
	if x not in n:
		valor += 1
print('Consoantes: ' + str(valor))
print('Vogais: ' + str(len(palavra)-valor))
