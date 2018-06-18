from funcoes import leia_tupla
from funcoes import leia_lista
from funcoes import leia_dic
from funcoes import Pessoa, leia_obj

print('funcao leia_tupla')
nome, idade = leia_tupla()

print(nome)
print(idade)

print('funcao leia_lista')
info = leia_lista()

print(info[0])
print(info[1])

print('funcao leia_dic')
dicionario = leia_dic()

print(dicionario['nome'])
print(dicionario['idade'])

print('funcao leia_obj')
pessoa = leia_obj()

print(pessoa.nome)
print(pessoa.idade)













