# Cálculo de desconto sobre o valor do produto
valor_produto = float(input('Digite o valor do produto: '))
desconto = int(input('Digite o valor do desconto aplicado em %: '))

valor_com_desconto = valor_produto * (desconto / 100)
valor_final = valor_produto - valor_com_desconto

print(f'Com um desconto aplicado de {desconto} % o valor final do produto é igual a R${valor_final:.2f}')



