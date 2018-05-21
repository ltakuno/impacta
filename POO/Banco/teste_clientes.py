from clientes import Cliente
from contas import Conta
from bancos import Banco
from contasEspeciais import ContaEspecial

banco01 = Banco("Tatu")

cli01 = Cliente("José da Silva", "111-1111")
cli02 = Cliente("Maria da Costa", "222-2222")
print (cli01.nome)
conta01 = ContaEspecial(123, [cli01, cli02], 200, 500)

banco01.abre_conta(conta01)
conta01.deposito(100)
conta01.saque(20)
conta01.deposito(100)
conta01.extrato()








