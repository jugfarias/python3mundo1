# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

maior = num1
menor = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

print('Maior número: {}\nMenor número: {}'.format(maior, menor))