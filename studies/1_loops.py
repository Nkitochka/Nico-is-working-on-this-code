def spaceFunction():
    print("\n")
    print('-' * 100)
    print('x' * 100)
    print('-' * 100)
    print('\n')
###########################################
for i in range(1, 10, 2):
    print(i)
else:
    print('\nIs this what u\'ve wanted?')

for i in range (1, 100, 5):
    pass

spaceFunction()
###########################################


###########################################
count_W = 0
while count_W < 10:
    print(count_W)
    
    if count_W == 6:
        print('This is the six!')
        break
    else:
        print('Still not the six!\n')

    count_W = count_W + 1

spaceFunction()
###########################################


###########################################
count_D = 0

print('Count by urself, tell the numbers u already now. BUT, keep in mind that I\'ll not let the even numbers pass! Also counting more than 25 is restricted by my rules! 0_0\n')

while count_D < 40:
    count_D = count_D + 1
    

    if count_D % 2 == 0:
        print(f'Evens are restricted, huh... *{count_D} is skipped, rules are not violated tough*')
        
        continue

    if count_D == 25:
        print('NOT THE 25!!!! U SH@#@@#G, STOP ALREADY!')
        break

    print(f"-Umm, {count_D}?")

spaceFunction()
############################################


############################################
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

spaceFunction()
############################################


############################################
x_number = 1
while x_number != 8:
    print("*" * x_number)
    x_number = x_number +1

spaceFunction()
############################################


############################################
for i in range (7):
    for x in range(8):
        print("# ", end="")
    
    print()

spaceFunction()
############################################


############################################
for i in range(11):
    print(f' {i} x {i} = {i * i}')

spaceFunction()
############################################


############################################
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']

for word in lst:
    print(word)

spaceFunction()
############################################


############################################
for i in range (0, 101):
    if i % 2 != 0:
        continue
    print(i)

spaceFunction()
############################################


############################################
for i in range (0, 101):
    if i % 2 == 0:
        continue
    print(i)

spaceFunction()
############################################


############################################
sum_of_nums = 0
for i in range(0, 101):
    sum_of_nums = sum_of_nums + i
    print(i)

print(sum_of_nums)
spaceFunction()
############################################


############################################
sumOfEvens = 0
sumOfOdds = 0

for i in range(0, 101):
    print(i)
    if i % 2 != 0:
        sumOfOdds = sumOfOdds + i
        continue
    if i % 2 == 0:
        sumOfEvens = sumOfEvens + i
        continue

print(f"Evens: {sumOfEvens}")
print(f"Odds: {sumOfOdds}")
