from random import randint

tentativas = 0
numero_aleatorio = randint(1, 10)

while True:
    numero_inserido = int(input('Digite um número: '))
    if numero_inserido == numero_aleatorio:
        print('Parábens você acertou!')
        break
    elif numero_inserido > numero_aleatorio:
        print('Número digitado muito alto! tente novamente')
    else:
        print('Você errou, continue tentando')