def calcular_estatistiscas(numeros):
    menor = numeros[0]
    maior = numeros[0]
    soma = 0
    cont = 0
    for n in numeros:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
        soma = soma + n
        cont = cont + 1

    media = soma/cont        
    return maior, menor, media, soma

def calcular_estatistiscas2(numeros):
    menor = min(numeros)
    maior = max(numeros)
    soma = sum(numeros)
    media = soma / len(numeros)

    return maior, menor, media, soma


assert(calcular_estatistiscas2([1,2,3]) == (3,1,2.0,6)) 
assert(calcular_estatistiscas2([2,2,2]) == (2,2,2.0,6)) 
assert(calcular_estatistiscas2([5,6,1]) == (6,1,4.0,12)) 



