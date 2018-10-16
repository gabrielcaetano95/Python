#!/usr/bin/python3

Prova1 = float(input('Valor 1a prova: '))*2
Prova2 = float(input('Valor 2a prova: '))*3
Prova3 = float(input('Valor 3a prova: '))*4
Prova4 = float(input('Valor 4a prova: '))
QntProvas = 4

Media = round((((Prova1)  + (Prova2)  + (Prova3)  + (Prova4))) / QntProvas,2)


if Media >= 7:
	print('Média = ' + str(Media) + ' / Aluno Aprovado')
elif Media >= 5:
	print('Média = ' + str(Media) + ' / Aluno em exame')
else:
	print('Média = ' + str(Media) + ' / Aluno reprovado')
