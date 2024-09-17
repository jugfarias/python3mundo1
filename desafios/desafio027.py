# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite seu nome completo: ')

nome_lista = nome.split()
comp = len(nome_lista)

print('{} {}'.format(nome_lista[0], nome_lista[comp - 1]))