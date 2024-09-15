# Faça um programa que leia a altura e a largura de uma parede, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

from math import ceil

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt

litros = area / 2

print('É necessário {}L de tinta para pintar {}m² de parede.'.format(ceil(litros), area))