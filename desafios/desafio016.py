# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

num = float(input('Digite um número decimal: '))

pt_inteira = trunc(num)

print('A parte inteira de {} é {}.'.format(num, pt_inteira))