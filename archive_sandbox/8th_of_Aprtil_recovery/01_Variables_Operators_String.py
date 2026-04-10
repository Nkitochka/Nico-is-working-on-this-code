import os

#START
greating = '''\n\tHello! Can i get some information about you? \nNeeded info:\n
1. Age\n2. Country\n3. Phone number\n4. Full name\n'''

print(greating)

# Variables
age = 0
country = ''
phone_number = 0
first_name = ""
last_name = ''
full_name = first_name + last_name


place_holder_input = input('Are you agree to give us this info? [Y\\N]\n').capitalize()


if place_holder_input == 'N':
    print('Hmm... okay, see you next time then.')
    
else:
    os.system('cls')
    while age == 0 or country == '' or phone_number == 0 or first_name == '' or last_name == '':
        print(f'Info --- |Age: {age}|  |Country: {country}|  |Name: {full_name}|  |Phone number: {phone_number}|')
        
        place_holder_input = input('What you would like to fill?\n').capitalize()
        os.system('cls')
        
        if place_holder_input == 'Name':
            first_name = input('First name: ')
            last_name = input('Last name: ')
            full_name = first_name.capitalize() + ' ' + last_name.capitalize()
            input('Thanks! ...Press enter to continue.')
            os.system('cls')
        
        
        elif place_holder_input == 'Age':
            age = int(input('Age: '))
            input('Thanks! ...Press enter to continue.')
            os.system('cls')
        
        elif place_holder_input == 'Country':
            country = input('Country: ').capitalize()
            input('Thanks! ...Press enter to continue.')
            os.system('cls')
            
        elif place_holder_input == 'Phone number':
            phone_number = int(input('Give last 5 digits of your phone number: '))
            input('Thanks! ...Press enter to continue.')
            os.system('cls')
            
    os.system('cls')
    print('''\tWell, seems like you gave us all the info.
Thanks for your cooperation, we will connect you again.
Wait for call at the last days of next weekend. Goodbye!''')