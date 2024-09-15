# Faça um programa que leia um número inteiro e mostre na tela a sua tabuada.

n = int(input('Digite um número inteiro: '))

print('Tabuada do {}'.format(n))

for i in range (1, 11):
    print('{} x {} = {}'.format(i, n, i*n))