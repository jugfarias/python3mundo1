# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade em km/h: '))
limite = 80

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('Você foi multado. R${:.2f}'.format(multa))
else:
    print('Passar bem.')