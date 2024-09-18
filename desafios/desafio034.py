# Escreva um programa que leia o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Salário: R$'))

if salario > 1250:
    salario += salario * 0.1
else:
    salario += salario * 0.15

print('O novo salário é de: {}'.format(salario))