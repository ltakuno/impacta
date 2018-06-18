import funcoes

assert (funcoes.somar(5, 5) == 10)
assert (funcoes.somar(2, 3) == 5)
assert (funcoes.somar(2, 5) == 7) 
assert (funcoes.somar(-2, 5) == 3)
assert (funcoes.potencia(2, 3) == 8)
assert (funcoes.potencia(10, 4) == 10000)
assert (funcoes.numero_par(2) == True)
assert (funcoes.numero_par(7) == False)

assert (funcoes.fatorial(1) == 1)
assert (funcoes.fatorial(2) == 2)
assert (funcoes.fatorial(3) == 6)
assert (funcoes.fatorial(4) == 24)
assert (funcoes.fatorial(5) == 120)
assert (funcoes.fatorial(6) == 720)

try:
    funcoes.fatorial('132')
except AssertionError as e:
    print('Valor invalido no parâmetro', e)

    
print('imprimindo número de 1 a 5')
funcoes.sequencia(1,5)
print('imprimindo número de 5 a 10')
funcoes.sequencia(5,10)
