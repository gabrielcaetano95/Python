#!/usr/bin/python3

import sys


alfabeto = 'abcdefghijklmnopqrstuvwxyz'


def cript(mensagem):
	novo = ''
	chave = 3
	for c in mensagem:
		if c in alfabeto:
			indice = alfabeto.index(c)
			novo = novo + alfabeto[(indice + chave) % len(alfabeto)]
		else:
			novo += c
	print(novo)

def decript(mensagem):
	novo = ''
	chave = -3
	for c in mensagem:
		if c in alfabeto:
			indice = alfabeto.index(c)
			novo = novo + alfabeto[(indice + chave) % len(alfabeto)]
		else:
			novo += c
	print(novo)



def main():

	try:
		tipo = sys.argv[1].lower()
		mensagem = sys.argv[2].lower()

		dicionario = {'cript':cript,'decript':decript}

	except IndexError as e:
		print('Preencher tipo(cript ou decript) e mensagem(livre)')

	try:
		dicionario[tipo](mensagem)
		
	except KeyError as e:
		print('Tipo "' + tipo + '" inválido')

if __name__ == '__main__':
	main()