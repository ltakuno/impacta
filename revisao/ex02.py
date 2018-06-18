Lista=[6,5,3,2,1,9,7,4]
numero = int(input('Digite um número:'))


#verificar se o número digitado está na lista ou não
for n in Lista:
    if (n == numero):
        print('O elemento pertence a lista')
        break
else:
    print('O elemento não pertence a lista')
    
