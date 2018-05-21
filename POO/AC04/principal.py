from funcoes_cadastro import menu 
from funcoes_cadastro import cadastrar_alunos 
from funcoes_cadastro import listar_alunos_curso 
from funcoes_cadastro import listar_alunos_por_ano 
from funcoes_cadastro import terminar_programa 

def main():
    alunos = []
    sair = 'n'
    while sair == 'n':
        opcao = menu()
        if (opcao == 1):
            cadastrar_alunos(alunos)
        elif (opcao == 2):
            listar_alunos_curso(alunos)
        elif (opcao == 3):
            listar_alunos_por_ano(alunos)
        elif (opcao == 4):
            sair = terminar_programa()
        
main()
