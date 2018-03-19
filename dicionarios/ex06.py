def construir_tabela():
    quadrados = {}
    for i in range(101):
        quadrados[i] = i * i

    return quadrados




tabela = construir_tabela()
print (tabela)
