from funcoes import numero_par

numero = int ( input('Digite um numero: '))

if (numero_par(numero) == True):
    print('O número é par')
else:
    print('O número é impar')
