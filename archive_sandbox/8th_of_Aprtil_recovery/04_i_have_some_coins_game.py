# Imports
import random
import time
import os 

# Variables

hp = 100
gold = 0
choice = 0
# Functions
def handle_event(hp, gold):
    
    time.sleep(2)
    rand_event = random.randint(0, 2)
    
    if rand_event == 0:
        print('Phew... Nothing bad happened at least.')
        time.sleep(3)
        
    elif rand_event == 1:
        print('You\'ve encounter an enemy!')
        loading()
        randamage = random.randint(5, 35)
        hp -= randamage
        print(f'You took {randamage} damage!')
        time.sleep(3)
        
    elif rand_event == 2:
        print('You have found one gold!')
        gold += 1
        time.sleep(3)
    
    return hp, gold
        
def loading():
    spinner = ['|', '/', '-', '\\']
        
    for i in range(20):
        print(f'\rBattle ongoing {spinner[i % len(spinner)]}...', end = "")
        time.sleep(0.15)
    os.system('cls')

def stats(hp, gold):
    print()
    print("S> ", '-' * 17)
    print("T> ", '|', ' '*3, f'HP:{hp}', ' '*2, '|')
    print("A> ", '-' * 17)
    print("T> ", '|', ' '*2, f'GOLD:{gold}', ' '*3, '|')
    print("S> ", '-' * 17)
    

# Main code
while hp > 0:
    stats(hp, gold)
    print('\n')
    choice = input('1 - Explore(Random event) | 2 - Rest (+HP) | 3 - Quit  ').lower()
    time.sleep(1)
    os.system('cls')
    
    if choice == '1' or choice == 'explore':
        hp, gold = handle_event(hp, gold)
        os.system('cls')
        
    elif choice == '2' or choice == 'rest':
        heal = random.randint(5, 10)
        hp += heal
        print(f'You have healed {heal}.')
        os.system('cls')
    
    elif choice == '3' or choice == 'quit':
        break
    
print('Game over. Thanks for playing!')