#!/usr/bin/python3

#print('Olá Mundo')
velocidade = int(input('Digite a velocidade: '))
#velocidadeex = int((velocidade-110)*5)

if velocidade > 110:
	print('Você foi multado. Valor da multa = R$' + str((velocidade-110)*5) + ',00')
else:
 	print('Velocidade permitida')

#print('Olá, meu nome é ' + nome + ', e tenho ' + str(idade) + ' anos')
