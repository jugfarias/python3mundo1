# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex:
# Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = input('Digite um número de 0 a 9999: ')

if len(numero) < 4:
    intervalo = 4 - len(numero)
    for i in range (intervalo):
        numero = '0' + numero
    
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(unidade, dezena, centena, milhar))

