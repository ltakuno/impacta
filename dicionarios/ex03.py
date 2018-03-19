profissoes = {'Pedro': 'encanador',
              'Maria': 'encanadora',
              'Antônio': 'eletricista',
              'Cintia' : 'médica',
              'Paulo': 'engenheiro'}

for nome in profissoes:
    if (profissoes[nome] == 'encanador' or profissoes[nome] == 'encanadora'):
        print(nome)
