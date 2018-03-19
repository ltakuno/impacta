def extrair_chaves(dicionario):
    lista_chaves = []

    for chave in dicionario:
        lista_chaves.append(chave)

    return lista_chaves


def teste_funcao01():
    lista1 = extrair_chaves({'a' : 1, 'b' : 2, 'c' : 3})
    lista1.sort()
    assert(lista1 == ['a', 'b', 'c'])

def teste_funcao02():
    lista1 = extrair_chaves({1111:'Alfredo', 2222: 'Pedro', 3333: 'Maria'})
    lista1.sort()
    assert(lista1 == [1111,2222,3333])



teste_funcao01()
teste_funcao02()
