from contas import Conta

class ContaEspecial(Conta):
    def __init__(self, numero, clientes, saldo = 0, limite = 0):
        super().__init__(numero, clientes, saldo)
        self.limite = limite

    def saque(self, valor):
        if (self.saldo + self.limite >= valor):
            self.saldo -= valor
            self.operacoes.append(("SAQUE", valor))
