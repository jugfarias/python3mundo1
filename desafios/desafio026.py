# Faça um programa que leia uma frase pelo teclado e mostre:
#  - Quantas vezes aparece a letra "A"
#  - Em que posição ela aparece a primeira vez
#  - Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')
frase = frase.lower()

print('Quantidade de letras a na frase: {}'.format(frase.count('a')))
print('Primeira aparição da letra a foi na posição: {}'.format(frase.find('a')))
print('Última aparição da letra a foi na posição: {}'.format(frase.rfind('a')))
