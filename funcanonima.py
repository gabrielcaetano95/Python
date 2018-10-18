#!/usr/bin/python3

#list = [2,3,4,5,6,7,8,9,10]

quadrados = list(map(lambda x: x ** 2, range(1,11)))

print(quadrados)


a = lambda x : x ** 2
list = []

#----------------------------
for x in range(1,11):
    list.append(a(x))

#----------------------------
for x in range(1,11):
    list.append((lambda x : x ** 2)(x))

#----------------------------

lista = [(lambda x : x ** 2)(x) for x in range(1,11)]
