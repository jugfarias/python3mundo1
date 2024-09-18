# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = input('Digite um ano qualquer: (Coloque 0 para analisar o ano atual) ')

if ano == '0':
    ano = str(date.today().year)

final = int(ano[len(ano) - 2] + ano[len(ano) - 1])
ano = int(ano)

if final == 0:
    if ano % 400 == 0:
        print('Ano bissexto')
    else:
        print('Ano normal')
elif final % 4 == 0:
    print('Ano bissexto')
else:
    print('Ano normal')

