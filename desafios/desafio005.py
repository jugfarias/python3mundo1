# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor.

n = int(input('Digite um número inteiro: '))

ant = n - 1
suc = n + 1

print('O antecessor e sucessor do número {} são: {} e {}'.format(n, ant, suc))