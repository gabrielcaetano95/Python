#!/usr/bin/python3

try:
	linguagem = input('Qual a linguagem de programação?')

	if linguagem.lower().strip() != 'python':
		raise ValueError('Resposta Errada')
	else:
		print('Resposta Correta')

except ValueError as e:
	print(e)