# Esrceva um programa que leia uma temperatura em graus celsius e converta para graus Fahrenheit (C × 9/5) + 32

c = float(input('Digite a temperatura em ºC: '))

f = (c * 9 / 5) + 32

print('{}ºC é {}ºF'.format(c, f))