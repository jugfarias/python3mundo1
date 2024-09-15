# Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento.

salario = float(input('Digite o salário atual: '))
aumento = int(input('Em quanto por cento (%) deve aumentar? '))

salario_novo = salario + salario * (aumento / 100)

print('O salário do funcionário passa de {} para {} com {}% de aumento.'.format(salario, salario_novo, aumento))