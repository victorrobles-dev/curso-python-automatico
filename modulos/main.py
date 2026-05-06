from exercicios.matematica import dobro, metade
from exercicios.mensagens import bem_vindo
# from modulos.funcoes import saudacao, somar, subtrair
# saudacao('Victor')
# somar(2, 5)
# subtrair(10, 4)
numero = int(input('Digite um número e vou exibir o dobro: '))
dobro(numero)

numero = int(input('Digite um número e vou exibir a metade: '))
metade(numero)

nome = input('Digite o seu nome: ')
bem_vindo(nome)