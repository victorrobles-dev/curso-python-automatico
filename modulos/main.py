from exercicios.matematica import dobro, metade
from exercicios.mensagens import bem_vindo
from exercicios.meu_pacote.formatador import caixa_alta 
from exercicios.meu_pacote.numeros import eh_par

numero = int(input('Digite um número e vou exibir o dobro: '))
dobro(numero)

numero = int(input('Digite um número e vou exibir a metade: '))
metade(numero)

nome = input('Digite o seu nome: ')
bem_vindo(nome)

caixa_alta('texto em maiúsculo')

eh_par(10)