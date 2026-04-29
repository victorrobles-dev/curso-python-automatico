# Aula sobre funções 

# def saudacao(nome):
#     print(f'Olá {nome} seja bem vindo!')
# saudacao('Victor')

# def somar(num1, num2):
# #     resultado = num1 + num2
# #     print(f'A soma entre o número {num1} e {num2} é igual a {resultado}')
# # somar(7, 14)

def calcular_desconto(valor, percentual):
    desconto = valor * (percentual / 100)
    valor_final = valor - desconto
    return valor_final

print(calcular_desconto(1000, 10))
