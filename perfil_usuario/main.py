from perfil import usuario

nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

if usuario.validar_idade(idade):
    perfil_usuario = usuario.criar_perfil(nome, idade)
    print('Perfil criado')
else:
    print('Acesso negado')