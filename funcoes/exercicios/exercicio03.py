# Crie uma função chamada verificar_par(numero) que retorna: "Par" se o número for par | "Ímpar" se for ímpar | Peça um número ao usuário com input(), chame a função e mostre o resultado.
def verificar_par(numero):
    if numero % 2 == 0:
        return (f'O número {numero} é par')
    else:
        return (f'O número {numero} é ímpar')
    
numero_inserido = int(input('Digite um número: '))
print(verificar_par(numero_inserido))