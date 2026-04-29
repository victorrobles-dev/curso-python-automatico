# Verificador de Nota Mínima: Crie um código que pergunte ao usuário qual foi sua nota em um teste. Defina uma nota mínima para aprovação (por exemplo, 6). Use uma estrutura if para verificar se a nota do usuário é maior ou igual à nota mínima. Se for, exiba a mensagem "Você atingiu a nota mínima!".

notaMinima = 7
notaTeste = float(input('Digite a nota que você tirou no teste: '))

if notaTeste >= 7:
    print('Você atingiu a nota mínima')