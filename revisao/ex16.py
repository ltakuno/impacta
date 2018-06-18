valores = {1: 'Pedro',
           2: 'Jose',
           3: 'Pedro',
           4: 'Maria',
           5: 'André'}
maior = -1
menor = 10000

for i in valores:
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print('maior valor: %d' % (maior))
print('menor valor: %d' % (menor))

