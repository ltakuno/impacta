import sys
nome = sys.argv[1]
texto = []
try:
    arq = open(nome, 'r')
except IOError:
    print ('Nao foi possivel abrir o arquivo!')
else:
    texto = arq.readlines()
    arq.close()

if texto:
    print(texto)