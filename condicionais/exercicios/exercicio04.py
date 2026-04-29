# Peça ao usuário uma nota de 0 a 10 para um filme. Classifique a avaliação assim: Nota 9 ou 10: "Excelente!" | # Nota 7 ou 8: "Muito bom" | # Nota 5 ou 6: "Regular" | # Menor que 5: "Ruim"

nota = int(input('Digite uma nota para o filme assistido: '))

if nota >= 9:
    print('Excelente!')
elif nota >= 7:
    print('Muito bom')
elif nota >= 5:
    print('Regular')
else:
    print('Ruim')