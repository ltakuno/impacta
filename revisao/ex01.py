Lista=[6,5,3,2,1,9,7,4]
numero = int(input('Digite um número:'))

#verificar se o número digitado está na lista ou não
i = 0
achou = False

while i < len(Lista):
    if (Lista[i] == numero):
        achou = True
    i = i + 1

if (achou == True):
    print('O elemento pertence a lista')
else:
    print('O elemento não pertence a lista')
