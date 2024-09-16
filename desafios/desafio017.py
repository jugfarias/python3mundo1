# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

h = sqrt(co ** 2 + ca ** 2)

print('A hipotenusa do triângulo é: {}.'.format(h))