agenda = {'Antonio' : '123-4567', 
          'Rui': '444-3546', 
          'alberto': '222-2222',
          'joana': '3022-2233',   
          'ALfredo': '333-3333'}

for (nome, telefone) in agenda.items():
    if (nome[0] == 'A' or nome[0] == 'a'):
        print('%s: %s' % (nome, telefone))
