PAR = []
IMPAR = []

for i in range(20):
    n = int(input("Digite um número:"))
    if (n % 2 == 0):
        PAR.append(n)
    else:
        IMPAR.append(n)

print('O vetor par é:', PAR)
print('O vetor ímpar é:', IMPAR)


