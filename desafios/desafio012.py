# Faça um algoritmo que leia um preço de um produto e mostre o seu novo preço com 5% de desconto.

preco = float(input('Digite o preço do produto: '))
desconto = int(input('Quanto % de desconto? '))

preco_novo = preco - preco * (desconto / 100)

print('O produto com {}% de desconto fica: R${:.2f}.'.format(desconto, preco_novo))