# Elegibilidade para um Evento (Idade Mínima): Imagine um evento para maiores de 15 anos. Crie um código que pergunte a idade do usuário. Verifique se a idade do usuário é maior ou igual a 15. Se for, exiba "Você pode participar do evento!".

age = int(input('Digite a sua idade atual: '))

if age >= 15:
    print('Você pode participar do evento!')