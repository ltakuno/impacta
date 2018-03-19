numeros = [5,2,1,6,7,8,9,20,24]

maior = numeros[0]
menor = numeros[0]
contador = 0
total = 0
for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    total  = total + n
    contador = contador + 1


media = total / contador

print('O maior elemento: %d ' % (maior))
print('O menor elemento: %d ' % (menor))
print('A média : %d' % (media))
