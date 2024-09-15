n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
mult = n1 * n2
div = n1 / n2
div_int = n1 // n2
exp = n1 ** n2

# \n para pular a linha dentro do print
print('A soma é {}, \n o produto é {} e \n a divisão é {:.2f}'.format(soma, mult, div), end = '. ') # end = ' ' para ficar na mesma linha
print('A divisão inteira é {} e a potência é {}'.format(div_int, exp))