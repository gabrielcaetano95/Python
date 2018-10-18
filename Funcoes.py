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

	tipo = sys.argv[1].lower()
	mensagem = sys.argv[2].lower()

	#print(tipo, mensagem)

	if tipo == 'cript':
		cript(mensagem)
	elif tipo == 'decript':
		decript(mensagem)
	else:
		print('comando invalido')





if __name__ == '__main__':
	main()


	#------------------------------------------------------

# 	def escopo(nome,idade=18):
# 	return 'nome {n} idade: {i}'.format(n=nome,i=idade)
# 	#ou print
# print(escopo('gabriel',23))