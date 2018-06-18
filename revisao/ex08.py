from funcoes import potencia


b = int(input('Digite a base:'))
e = int(input('Digite o expoente:'))

resultado = potencia(b, e)

print('%d elevado %d : %d' % (b, e, resultado))
        
