# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')
print(nome.upper())
print(nome.lower())

lista_nome = nome.split()
nome_sem_espacos = ''.join(lista_nome)
print('Número de letras no nome: {}'.format(len(nome_sem_espacos)))

print('Número de letras no primeiro nome: {}'.format(len(lista_nome[0])))