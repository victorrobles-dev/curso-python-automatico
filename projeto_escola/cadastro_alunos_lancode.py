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

def listar_alunos():
    if len(alunos) == 0:
        print(f'Sem alunos cadastrados')
        return
    for aluno in alunos:
        print(f'Nome: {aluno['nome']} \n Idade: {aluno['idade']} \n Nota: {aluno['nota']} \n {'='*30}')
    
def procurar_aluno(nome_aluno):
    if len(alunos) == 0:
        print(f'Sem alunos cadastrados')
        return
    for aluno in alunos:
        if aluno['nome'].lower() == nome_aluno.lower():
            print(f'Nome: {aluno['nome']} \n Idade: {aluno['idade']} \n Nota: {aluno['nota']}')
            break
    else:
        print(f'Esse aluno não foi encontrado!')

def remover_aluno(nome_aluno):        
    if len(alunos) == 0:
        print(f'Sem alunos cadastrados')
        return
    for aluno in alunos:
        if aluno['nome'].lower() == nome_aluno.lower():
            alunos.remove(aluno)
            print(f'{nome_aluno} foi removido com sucesso!')
            break
    else:
        print(f'Esse aluno não foi encontrado!')

def media_entre_alunos():
    if len(alunos) == 0:
        print(f'Sem alunos cadastrados')
        return
    soma = 0
    for aluno in alunos:
        soma += aluno['nota']
    media = soma / len(alunos)
    print(f'A média geral dos alunos é {media:.2f}')  

while True:
    opcao = int(input('\n Digite a opção que deseja executar: \n 1. Cadastrar aluno \n 2. Listar todos os alunos \n 3. Buscar aluno pelo nome \n 4. Remover aluno \n 5. Mostrar média geral entre alunos \n 6. Sair \n'))
    
    match opcao:
        case 1:
            adicionar_aluno()
        case 2:
            listar_alunos()
        case 3:
            nome_aluno = input('Qual aluno deseja buscar? ')
            procurar_aluno(nome_aluno)
        case 4:
            nome_aluno = input('Qual aluno deseja remover? ')
            remover_aluno(nome_aluno)
        case 5:
            media_entre_alunos()
        case 6:
            break