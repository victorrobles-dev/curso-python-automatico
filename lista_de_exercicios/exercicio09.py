# Calculadora simples
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
operador = input('Escolha o operador de sua preferência (+, -, *, /): ')

match operador:
    case '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    case '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    case '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    case '/':
        print(f'{num1} / {num2} = {num1 / num2}')
