class MinhaExcecao(Exception):
    pass

def funcao(x):
    if (x < 0 or x > 100):
        raise MinhaExcecao("Valor inválido!")


def caller(x):
    try:
        funcao(x)
    except MinhaExcecao as e:
        print('Erro na funcao tal!! ')
        print(e)

def main():
    funcao(130)


if __name__ == '__main__':
    main()



    


