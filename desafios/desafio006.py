# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digitie um número: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('O número escolhido foi: {} \nDobro: {}\nTriplo: {}\nRaiz quadrada: {}'.format(n, dobro, triplo, raiz))