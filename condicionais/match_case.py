opcao = int(input('Digite a opção desejada (1 a 3): '))

match opcao:
    case 1:
        print('Saque')
    case 2:
        print('Depósito')
    case 3:
        print('Extrato')
    case _:
        print('Opção inválida')