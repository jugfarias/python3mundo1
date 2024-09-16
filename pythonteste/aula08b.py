import random
import emoji

lista = ['banana', 'maracujá', 'uva', 'pêssego', 'amora']

aleatorio1 = random.choice(lista)
print(aleatorio1)

aleatorio2 = random.randint(0,10)
print(aleatorio2)

aleatorio3 = random.randrange(0,10)
print(aleatorio3)

aleatorio4 = random.shuffle(lista)
print(lista)

print(emoji.emojize(':snake:'))
print(emoji.emojize(':cat:'))
print(emoji.emojize(':fire:'))