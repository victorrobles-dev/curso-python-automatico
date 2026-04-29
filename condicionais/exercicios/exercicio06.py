# Crie um menu com 3 opções: 1. Pizza, 2. Sushi, 3. Salada. O usuário digita um número. O programa mostra o prato escolhido. Se digitar qualquer outro número, exiba: "Opção inválida."
menu = int(input('Digite o número da refeição disponível no cardápio: 1, 2 ou 3: '))

match menu:
    case 1:
        print('1. Pizza')
    case 2:
        print('2. Sushi')
    case 3:
        print('3. Salada')
    case _:
        print('Opção inválida')







