# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo.')