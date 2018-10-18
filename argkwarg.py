#!/usr/bin/python3

#args

def args(*args):
	'''A função traz todos os argummentos repassados'''
	print(args)


args('gabriel','23','bomdia')

------------------------------------------------------------

#kwargs

def kwargs(**kwargs):
		print(kwargs)

kwargs(nome='gabriel',idade='23',mensagem='bom dia')