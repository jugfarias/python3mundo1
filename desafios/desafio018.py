# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import cos, sin, tan

angulo = float(input('Digite um ângulo, em graus: '))

cos = cos(angulo)
sin = sin(angulo)
tan = tan(angulo)

print('Ângulo passado: {}º\nCosseno: {}\nSeno: {}\nTangente: {}'.format(angulo, cos, sin, tan))