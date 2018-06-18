profissoes = {'Pedro': 'encanador',
              'Maria': 'encanador',
              'Jose': 'eletricista',
              'Paulo': 'professor',
              'Antonio': 'contador'}


lista_encanadores = []

for nome in profissoes:
    if (profissoes[nome] == 'encanador'):
        lista_encanadores.append(nome)

print(lista_encanadores)
