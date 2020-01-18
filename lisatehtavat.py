#1
a=3
n=4

for i in range(n):
    print(a*i)

#2
import random

r1=random.randint(1, 10)

print(r1)

#3
nimet = ['Keijo', 'Reijo', 'Veijo']

for nimi in nimet:
    if nimi == 'Veijo':
        print(nimi)

#nimet.append('   ')

#4
a = 3

for i in [2, 3, 4]:
    a = a + i

b = a
b = b - a

print(b)
print(a)

#5

def osuma(p_healt, hit):
    return p_healt - hit

player_hp = 10
#player_hp = 20

rocket_hit_value = 4
pistol_hit_value = 1

player_hp = osuma(player_hp, rocket_hit_value)
player_hp = osuma(player_hp, pistol_hit_value)

if player_hp < 6:
    print('Critical healt! HP:' + str(player_hp))
else:
    print('Health ok')