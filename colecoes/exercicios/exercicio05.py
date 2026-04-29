# 
user = {
    'name': input('Digite o seu nome: '),
    'age': int(input('Digite a sua idade: '))
}

if user['age'] >= 18:
    print(f'Acesso liberado para: {user['name']}')
else:
    print(f'Acesso negado para: {user['name']}')