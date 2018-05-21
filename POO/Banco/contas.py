class Conta:
    def __init__(self, numero, clientes, saldo = 0):
        self.numero = numero
        self.clientes = clientes
        self.saldo = saldo
        self.operacoes = []

    def resumo(self):
        print('CC Número: {} Saldo: {:.2f}'.format(self.numero, self.saldo))

    def saque(self, valor):
        if self.saldo > valor:
           self.saldo -= valor
           self.operacoes.append(('SAQUE', valor))

    def deposito(self, valor):
        self.saldo += valor            
        self.operacoes.append(('DEPOSITO', valor))

    def extrato(self):
        print('Extrato CC Numero : %s \n' % (self.numero))

        for o in self.operacoes:
            print('%10s %10.2f' % (o[0], o[1]))

        print('\n Saldo: %.2f \n' % (self.saldo))

        
