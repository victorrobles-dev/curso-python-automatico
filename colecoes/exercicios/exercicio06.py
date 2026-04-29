#
credenciais_corretas = {
    'user': 'Victor',
    'password': 123456
}

credenciais_tentativa = {
    'user': input('Digite o seu usuário: '),
    'password': int(input('Digite a sua senha: '))
}

if credenciais_tentativa['user'] == credenciais_corretas['user'] and credenciais_tentativa['password'] == credenciais_corretas['password']:
    print('Login realizado com sucesso!')
else:
    print('Usuário ou senha incorretos, tente novamente!')