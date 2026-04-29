# Sistema de cofrinho
cofre = 0

while True:
    valor = float(input('Insira um valor no cofre: '))
    if valor == 0:
        break
    cofre += valor

print(f'O valor total guardado é: {cofre}')
        