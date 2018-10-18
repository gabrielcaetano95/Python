#!/usr/bin/python3
class Cliente():
    '''Criar um cliente no banco'''
    def __init__(self, titular, nconta,valorcc):
        self.titular = titular
        self.nconta = nconta
        self.valorcc = valorcc
    def saque(self, valor):
        if valor > self.valorcc:
            print('Saldo insuficiente')
        else:
            valoratual = self.valorcc - valor
            print('Valor Saque: {} \nSaldo em Conta: {}'.format(valor,valoratual))
    def deposito(self, valor):
        valoratual = self.valorcc + valor
        print('Valor Depositado: {} \nSaldo em Conta: {}'.format(valor,valoratual))

    def transferir(self, nome1,nome2,valor):
        if valor > nome1.valorcc:
            print('Saldo insuficiente')
        else:
            nome1.valorcc -= valor
            nome2.valorcc += valor
            print('Depositario: Valor Transferido: {} Saldo em Conta: {} \n'
                  'Creditado: Valor Recebido: {} Saldo em Conta: {}'
                  .format(valor,nome1.valorcc,valor,nome2.valorcc))

class Poupanca(Cliente):
    def __init__(self, titular, nconta,valorcc,valorpp):
        super().__init__(titular, nconta,valorcc)
        self.valorpp = valorpp

    def render_juros(self,valorpp):
        self.valorpp *= 1.005
        print('Valor Poupanca: {}'.format(round(self.valorpp,2)))

cliente1 = Cliente('Gabriel',1,150)
cliente2 = Poupanca('Camila',2,500,1000)

# print(cliente1.titular,cliente1.nconta,cliente1.valorcc)
print(cliente2.titular,cliente2.nconta,cliente2.valorcc,cliente2.valorpp)
#cliente1.saque(250)
#cliente2.deposito(300)
#cliente2.transferir(cliente2,cliente1,250)
cliente2.render_juros(cliente2.valorpp)