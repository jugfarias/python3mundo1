frase = 'Eu gosto de python'

print(frase)

#Fatiamento:
print(frase[4])
print(frase[12:18]) # vai do char 12 ao 17
print(frase[12:]) # vai até o final
print(frase[12:18:2]) # vai de 2 em 2
print(frase[9::3]) # começa no 9, vai até o final de 3 em 3
print(frase[::2]) # vai do início ao final de 2 em 2
print(frase[:2]) # vai do início 

# Funcionalidades:
print(len(frase)) # comprimento da string
print(frase.count('o')) # conta quantos 'o' aparecem na string
print(frase.count('o',0,11)) # conta quantos 'o' aparecem no fatiamento 0:11 da string
print(frase.find('py')) # retorna onde está 'python'
print(frase.find('nao')) # retorna -1

print('python' in frase) # retorna True
print('Ravena' in frase) # retorna False

# Transformação:
nova_frase = frase.replace('python', 'Ravena')
print(nova_frase)
nova_frase = frase.upper() # tudo maiúsculo
print(nova_frase)
nova_frase = frase.lower() # tudo minúsculo
print(nova_frase)
nova_frase = nova_frase.capitalize() # primeira letra maiúscula
print(nova_frase)
nova_frase = frase.title() # primeiras letras maiúsculas

frase_com_espaco = '  Python é legal ' # frase com espaços inúteis
print(frase_com_espaco)
print(frase_com_espaco.strip()) # retira os espaços inúteis
print(frase_com_espaco.rstrip()) # retira os espaços inúteis à direita apenas
print(frase_com_espaco.lstrip()) # retira os espaços inúteis à esquerda apenas

# Divisão:
lista = frase.split() # separa a string em elementos de uma lista, baseado nos lugares dos espaços, por padrão
print(lista)

# Junção
print('-'.join(lista))
print('*'.join(lista))


