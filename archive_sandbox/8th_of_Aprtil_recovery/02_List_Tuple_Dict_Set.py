import random, time, sys, os

def pokke():
    return random.randint(1, 15)

##############################################################################################################
# POKEMON has: (name input only), [attack, defence, speed, type can be generated], (rarity only gen)         #
####VARIABLES###############VARIABLES#####################VARIABLES########VARIABLES#########VARIABLES########
name = 'None'
attack = 1
defence = 1
speed = 1
health = 1
poke_types = ['Fire', 'Water', 'Electricity', 'Grass', 'Ghost']
current_type = random.choice(poke_types)

chance = random.random()
rarity = 'Common'
buff = 1
if chance <= 0.1:
    rarity = 'LEGENDARY'
    buff = random.randint(5, 10)
elif chance <= 0.35:
    rarity = 'Epic'
    buff = random.randint(3, 5)
elif chance <= 0.6:
    rarity = 'Rare'
    buff = random.randint(1 , 3)
##############################################################################################################
input('Hello! Lets create our own pokemon card! First, you will choose the name, in the end i will randomly pick rarity that will buff stats.\n(PS press enter to continue dialogue!)')
os.system('cls')

name = input('Nico: What is name of our brand new pokemon?\nYou: Lets call him... ').capitalize()
time.sleep(0.3)
input(f'Nico: Ooh a {name}! What an interesting and super weird name, i like it!')
time.sleep(0.3)
input('Nico: Are you sure about that name?\nYou: Ummm... ')
time.sleep(0.1)
input('Nico: Anyways, i don\'t care! Lets continue!')

time.sleep(1)
os.system('cls')

spinner = ['|', '/', '-', '\\']
for i in range(20):
    print(f'\rGenerating stats {spinner[i % len(spinner)]}', end = "")
    time.sleep(0.15)
os.system('cls')

time.sleep(2)
attack = pokke() * buff
defence = pokke() * buff
speed = pokke() * buff
health = pokke() * buff

print('And here\'s the rarity of our pokemon!...')
spinner = ['|', '/', '-', '\\']
for i in range(20):
    print(f'\rGenerating rarity {spinner[i % len(spinner)]}', end = "")
    time.sleep(0.15)
os.system('cls')

print(f'Pokemon has {rarity} rarity! This will buff your stats by {buff}!')

time.sleep(3)

os.system('cls')
print(f'Name is {name}.\nRarity: {rarity} rarity.\nAttack: {attack} points.\nHealth: {health} points.\nDefence: {defence} points.\nSpeed: {speed} points.\nType: {current_type}!')