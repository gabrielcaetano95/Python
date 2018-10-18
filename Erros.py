#!/usr/bin/python3


while True:
	try:
		x = int(input('Digite um número: '))
		y = int(input('Digite um número: '))

		print (x + y)

	except Exception:
		print('apenas numeros')


	#Erro com variável
	#except Exception as e:
	#	print('apenas numeros')

	finally:
		print('Encerrado')


-----------------------------------------------
#Erro variavel

try:
	print(nome)
except NameError as e:
	print(e)

-----------------------------------------------
#Erro tipo

try:
	n = 5
	print('numero: ' + n)
except TypeError as e:
	print(e)

-----------------------------------------------
#Erro index

try:
	nome = 'Gabriel'
	nome.index(8)
except IndexError as e:
	print(e)


