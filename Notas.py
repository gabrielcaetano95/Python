#!/usr/bin/python3

valor = float(input('Digite um valor: '))

#notas
n100 = valor // 100
aux = valor % 100

n50 = aux // 50
aux = aux % 50

n20 = aux // 20
aux = aux % 20

n10 = aux // 10
aux = aux % 10

n5 = aux // 5
aux = aux % 5

n2 = aux // 2
aux = aux % 2

m1 = int(aux) // 1
aux = float(aux - int(aux))

m50 = (aux * 100) // 50
aux = int(aux * 100) % 50

m25 = aux // 25
aux = float(aux) % 25

m10 = aux // 10
aux = float(aux) % 10

m5 = aux // 5
aux = float(aux) % 5


#Notas
print('N100 ' + str(n100))
print('N50 ' + str(n50))
print('N20 ' + str(n20))
print('N10 ' + str(n10))
print('N5 ' + str(n5))
print('N2 ' + str(n2))
print('m1 ' + str(m1))
print('m50 ' + str(m50))
print('m25 ' + str(m25))
print('m10 ' + str(m10))
print('m5 ' + str(m5))
#Moedas



print('resto ' + str(aux))

