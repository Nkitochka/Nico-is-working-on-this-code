import os
###################################################
vegs1 = ['tomato', 'potato', 'carrot', 'cabbage']
frus1 = ['orange', 'pineapple', 'apple']

vegs2 = ['pumkin', 'mushroom', 'onion']
frus2 = ['banana', 'cherry', 'mango', 'watermelon']

shelf1 = [vegs1, frus2]
shelf2 = [vegs2, frus1]
shelf3 = [vegs1, frus1]
shelf4 = [vegs2, frus2]

def display():
    print("-" *200)
    print("-" *92, "CabineT", "-" *100)
    print(f'First shelf: {shelf1[0:]}')
    print(f'Second shelf: {shelf2[0:]}')
    print(f'Third shelf: {shelf3[0:]}')
    print(f'Fourth shelf: {shelf4[0:]}')
    print("-" *200)

####################################################
####################################################
####################################################
print('WARNING! To continue dialogues press Enter!')
input()
os.system('cls')


print('Hello! Welcome to our humble shop! Get everything u need to buy!')
print('Our rules, unfortunately, let us to take only one thing and add it to bill.')
input()
os.system('cls')

display()
print()
print('Choose the shelf, pls!')

user_input = int( input())

os.system('cls')

if user_input == 1:
    print(shelf1[0:])
if user_input == 2:
    print(shelf2[0:])
if user_input == 3:
    print(shelf3[0:])
if user_input == 4:
    print(shelf4[0:])
elif user_input > 4 or user_input < 0:
    print('Error!')

print()
print('Choose, pls. Our rules, unfortunately, let us to take only one thing and add it to bill.')

user_input = input('Write a word in low register of what u wanna plus to the bill and buy\n')
print('Can i get the...')
