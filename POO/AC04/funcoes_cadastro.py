from Aluno import Aluno

def menu():
    print('Escolha uma das opcoes abaixo')
    print('1 - Cadastrar aluno')
    print('2 - Listar alunos de um curso')
    print('3 - Listar alunos de um determinado ano')
    print('4 - Terminar o programa')
    opcao = int(input('Digite sua opção:'))
    return opcao

def cadastrar_alunos(alunos):
    continuar_cadastro = 's'
    while continuar_cadastro == 's':
        nome = input('Nome do Aluno:')
        data_nasc = input('Data de nascimento (dd mm aaaa):')
        RA = input('RA:')
        curso = input('Curso:')

        a1 = Aluno(nome, data_nasc, RA, curso)
        alunos.append(a1)

        continuar_cadastro = input('Mais alunos? (s/n):')

def listar_alunos_curso(alunos):
    print('Listagem de alunos por curso')
    curso = input('Digite o nome do curso: ')
    for aluno in alunos:
        if aluno.curso == curso:
            print('%s   %10s' % (aluno.nome, aluno.RA))
    

def listar_alunos_por_ano(alunos):
    print('Listagem de alunos por ano de nascimento')
    ano = input('Digite o ano de nascimento: ')
    for aluno in alunos:
        if aluno.obter_ano_nascimento() == ano:
            print('%s   %10s' % (aluno.nome, aluno.RA))

def terminar_programa():
    print('Você escolheu sair do programa.')
    sair = input('Confirma sair? (s/n):')
    return sair
