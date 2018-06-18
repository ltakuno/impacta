from funcoes import somar


n1 = int(input('Digite o número 1:'))
n2 = int(input('Digite o número 2:'))
total = somar(n1, n2)
print('A soma entre %d e %d : %d' % (n1, n2, total))
