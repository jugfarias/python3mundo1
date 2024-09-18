# trabalhando com cores no terminal

# \033[<estilo>;<cor_texto>;<cor_bg>m]

'''
códigos de estilo:
0: nada
1: negrito
4: underline
7: negativo

códigos de cor do texto:
30: branco
31: vermelho
32: verde
33: amarelo
34: azul
35: magenta
36: ciano
37: cinza

códigos de cor do bg:
40: branco
41: vermelho
42: verde
43: amarelo
44: azul
45: magenta
46: ciano
47: cinza
'''

print('\033[31mOlá mundo em vermelho\033[m')
print('\033[1;32;43mBrasil\033[m')

print('\033[mteste') # volta ao normal


# códigos no format:
nome = 'Ju'

print('Prazer te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m')) 


# uso de dicionário:
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
        }

print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['azul'], nome, cores['limpa']))

print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))