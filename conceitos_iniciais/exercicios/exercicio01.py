# Crie um código onde é solicitado para o usuário inserir dois valores: o ano atual, e o ano de nascimento. O sistema deve calcular quantos anos ele tem de acordo com essas informações e exibir no console.
anoAtual = int(input("Digite o ano atual: "))
anoNascimento = int(input("Digite o ano de seu nascimento: "))

idadeAtual = anoAtual - anoNascimento

print(f"De acordo com o ano atual e seu ano de nascimento sua idade é: {idadeAtual} anos de idade")