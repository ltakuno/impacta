def potencia(base, expoente):
    return base ** expoente

def somar(x, y):
    return x + y

def celsiu2Fahrenheit(graus):
    return 9/5.0 * graus + 32.0

def numero_par(numero):
    if (numero % 2 == 0):
        return True
    else:
        return False

def fatorial(n):
    assert(type(n) is int)
    r = 1
    for i in range(1, n+1):
        r = r * i
    return r

def sequencia(x, y):
    assert((x < y) == True)
    for n in range(x, y+1):
        print(n)

def leia_tupla():
    nome = input('Digite o nome:')
    idade = int(input('Digite a idade:'))

    return (nome, idade)

def leia_lista():
    nome = input('Digite o nome:')
    idade = int(input('Digite a idade:'))
    return [nome, idade]

def leia_dic():
    nome = input('Digite o nome:')
    idade = int(input('Digite a idade:'))

    return {'nome': nome, 'idade': idade }

class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade


def leia_obj():
    nome = input('Digite o nome:')
    idade = int(input('Digite a idade:'))

    return Pessoa(nome, idade)
    

def exercicio_tupla(n):
    assert(type(n) is int)
    assert(n >= 100 and n <= 1000)
    centenas = n / 100
    dezenas = (n % 100) / 10
    unidades = n % 10
    return (centenas, dezenas, unidades)
    


