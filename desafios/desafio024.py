# Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = input('Digite o nome de uma cidade: ')
cidade = cidade.lower()
'''
cidade_lista = cidade.split()

if cidade_lista[0] == 'santo':
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')
'''
print(cidade[0:5] == "santo")