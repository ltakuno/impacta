from Pessoa import Pessoa
from Conta import Conta

pessoas = []
continuar = 's'

while continuar == 's':
    nome = input('Digite o nome:')
    endereco = input('Digite o endereco:')
    idade = int(input('Digite a idade:'))

    possui_conta = input('A pessoa conta? (s/n):')

    if (possui_conta == 's'):
        numero_conta = input('Digite o numero da conta:')
        saldo = float(input('Digite o saldo:'))
    else:
        numero_conta = ''
        saldo = 0

    p1 = Pessoa()
    p1.setNome(nome)
    p1.setEndereco(endereco)
    p1.setIdade(idade)

    if (possui_conta == 's'):
        conta = Conta(numero_conta, saldo)
        p1.setConta(conta)
                      
    pessoas.append(p1)

    continuar = input('Deseja continuar? (s/n):')
    

for p in pessoas:
    p.imprimir_dados()



