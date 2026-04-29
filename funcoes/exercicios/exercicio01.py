# Crie uma função chamada quadrado(numero) que recebe um número como argumento e retorna o quadrado dele.
def quadrado(numero):
    quadrado_numero = numero ** 2
    return quadrado_numero

numero_inserido = int(input('Digite um número: '))

quadrado(numero_inserido)
print(f'A exponenciação do número {numero_inserido} é igual a {quadrado(numero_inserido)}' )