class Pessoa:
    def __init__(self, nome = '', endereco = '', idade = 0, conta = None):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.filhos = []
        self.conta = conta

    def imprimir_dados(self):
        print(self.__nome)
        print(self.__endereco)
        print(self.__idade)
              
    def setNome(self, nome):
        self.__nome = nome

    def setEndereco(self, endereco):
        self.__endereco = endereco
        
    def setIdade(self, idade):
        self.__idade = idade

    def adicionar_filhos(self, filho):
        self.filhos.append(filho)

    def mostrar_filhos(self):
        print ('Filhos de %s' % (self.__nome))
        for filho in self.filhos:
            filho.imprimir_dados()

    def setConta(self, conta):
        self.conta = conta
        
