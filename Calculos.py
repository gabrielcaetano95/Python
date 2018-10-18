#!/usr/bin/python3


def soma(a,b):
	z = a + b
	return z

def subt(a,b):
	z = a - b
	return z

def mult(a,b):
	z = a * b
	return z

def div(a,b):
	z = a // b
	y = a % b
	return 'quo ' + str(z) + '\n' + 'rest ' + str(round(y))



def calculo():

	n1 = float(input('1o numero: '))
	n2 = float(input('1o numero: '))
	operador = input('operador: ')

	operadores = {'soma':soma,
				  'subt':subt,
				  'mult':mult,
				  'div':div}

	print(operadores[operador](n1,n2))



if __name__ == '__main__':
	calculo()

