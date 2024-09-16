# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = input('Digite seu nome completo: ')
nome = nome.lower()

nome_lista = nome.split()

intervalo = len(nome_lista)

for i in range (0, intervalo):
    if (nome_lista[i]) == 'silva':
        print('Tem Silva no nome')
        break
    elif i == intervalo - 1:
        print('Não tem Silva no nome')
        break 