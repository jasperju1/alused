
# Kirjuta programm, mis küsib kasutajalt raadiuse 
# ja arvutab ringi pindala ja ümbermõõdu. (math.pi)

import math

r = float(input('Sisesta ringi raadius sentimeetrites: '))

c = 2 * math.pi * r
s = math.pi * r * r

print('Raadius: ', r, 'cm')
print('Pindala: ', round(s, 1), 'cm')
print('Ümbermõõt: ', round(c, 1), 'cm')
