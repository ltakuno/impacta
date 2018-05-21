from math import sqrt

try:
    num = float(input('Digite um numero:'))
    resultado = sqrt(num)
    print ('A raiz quadrada de %.1f: %.1f' % (num, resultado) )
except ValueError:
    print('Não é possível tirar a raiz quadrada!')
except Exception:
    print('Erro desconhecido!!')




