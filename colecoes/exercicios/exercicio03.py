# Trabalhando com contagem e localização - Mostre: Quantas vezes o nome Carla aparece, 
# Qual o índice da primeira vez que ele aparece

nomes = [ "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Fernando", "Giovana", "Hugo", "Isabela", "João", "Carla", "Lucas", "Mariana", "Nuno", "Olivia", "João", "Pedro", "Carla", "Rafael", "Ana" ]

contagem = nomes.count('Carla')
index = nomes.index('Carla')

print(f'O nomer Carla aparece {contagem} vezes na lista e aparece pela primeira vez no index {index}')