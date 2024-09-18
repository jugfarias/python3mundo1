# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

dist = float(input('Distância da viagem em km: '))

if dist <= 200:
    valor = dist * 0.5
else:
    valor = dist * 0.45

print('O valor total da viagem é: {}'.format(valor))