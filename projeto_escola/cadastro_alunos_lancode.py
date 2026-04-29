# Projeto cadastro de alunos

alunos = []

def adicionar_aluno():
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    while True:
        nota = float(input('Digite a nota do aluno: '))
        if nota >= 0 and nota <= 10:
            break
        else:
            print('Nota inválida, a nota deve ser de 0 a 10')

    dados = {
        'nome': nome,
        'idade': idade,
        'nota': nota
    }

    alunos.append(dados)

def listar_alunos(alunos):
    for aluno in alunos:
        print(f'Nome: {alunos['nome']} \n Idade: {alunos['idade']} \n Nota: {alunos['nota']} \n {'='*30}')

while True:
    opcao = int(input('Digite a opção que deseja executar: \n 1. Cadastrar aluno \n 2. Listar todos os alunos \n 3. Buscar aluno pelo nome \n 4. Consultar aluno \n 5. Mostrar média geral entre alunos \n 6. Sair \n'))
    
    match opcao:
        case 1:
            adicionar_aluno()
        case 2:
            listar_alunos()
        case 3:
            ...
        case 4:
            ...
        case 5:
            ...
        case 6:
            break

    