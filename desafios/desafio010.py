# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (considere US$1,00 = R$3,27)

rs = float(input('Quanto você tem na carteira? '))

us = rs / 3.27

print('Com R${:.2f} é possível comprar US${:.2f}'.format(rs, us))