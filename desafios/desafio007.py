# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('Abaixo, inserir as informações do aluno:')
nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1 + n2) / 2

print('{} ficou com média {}'.format(nome, media))