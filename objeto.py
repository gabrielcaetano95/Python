#!/usr/bin/python3

class Dog():
    '''Criar um cachorro'''
    def __init__(self, nome,raca,idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 100
    def latir(self):  
        '''Método para o cachorro latir'''
        print('{} Latindo...'.format(self.nome))

    def andar(self):
        '''Método para o cachorro andar'''
        andar = 40
        energiaatual = self.energia

        for x in range(1,andar):
            energiaatual -= 1
            print('{}%'.format(energiaatual))

    def dormir(self):
        '''Método para o cachorro dormir'''
        energiaatual = 100
        print(energiaatual)

dog1 = Dog('kid','rotweiller',2)
dog2 = Dog('python','poddle',3)

print(dog1.nome,dog1.idade,dog1.raca, sep='\n')
dog1.latir()
dog1.andar()
dog1.dormir()
#print(dog2.nome,dog2.idade,dog2.raca, sep='\n')