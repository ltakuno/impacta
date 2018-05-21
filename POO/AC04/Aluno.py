class Aluno:
    def __init__(self, nome = '', data_nasc = '', RA = '', curso = ''):
        self.nome = nome
        self.data_nasc = data_nasc
        self.RA = RA
        self.curso = curso

    def obter_ano_nascimento(self):
        return self.data_nasc.split()[2]
    
