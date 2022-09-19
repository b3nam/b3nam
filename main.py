#This program created by b3nam.
# version 1.00

import random
import string
import os

settings = {
    "length": '',
    "upper": 'y',
    "lower": 'y',
    "symbol": 'y',
    "number": 'y',
    "space": 'n'
}

def get_user_setting(settings):
    print()
    for options, values in settings.items():
        while True:
            if options != "length":
                user_input = (input(f"Would you use any {options} in your password(y/n)? : "))
                if user_input.isalpha() and user_input in ['y', 'n']:
                    if user_input ==  'y':
                        settings[options] = True
                        break
                    elif user_input == 'n':
                        settings[options] = False
                        break
                else:
                    print('Invalid input!!!')
            elif options == 'length':
                user_input = (input(f"Enter a length for your password: "))
                if user_input.isdigit() and 6 < int(user_input) < 20:
                    settings[options] = int(user_input)
                    break
                else:
                    print("Invalid input!!!")
    return settings

def get_random_upper_case():
    return random.choice(string.ascii_uppercase)

def get_random_lower_case():
    return random.choice(string.ascii_lowercase)

def get_random_symbol():
    return random.choice(string.punctuation)

def get_random_number():
    return random.choice(string.digits)

def generate_random_char(choices):
    choice = random.choice(choices)

    if choice == 'upper':
        return get_random_upper_case()
    if choice == 'lower':
        return get_random_lower_case()
    if choice == 'symbol':
        return get_random_symbol()
    if choice == 'number':
        return get_random_number()
    if choice == 'space':
        return ' '

def password_generator():
    os.system('cls')
    get_user_setting(settings)
    ans = ''
    final_password = ''
    password_length = settings['length']
    choices = list(filter(lambda x: settings[x], ['upper', 'lower', 'symbol', 'number', 'space']))
    for i in range(password_length):
        final_password += generate_random_char(choices)
    print(f'\nYour password is : {final_password}\n')
    while True:
        ans = input('Do you want to change generation?' 
                                '(for change setting type(s) & for change password type(p) and for done type(d) ')
        if ans.isalpha() and  ans in ['s', 'p', 'd']:
            if ans == 's':
                return password_generator()
            elif ans == 'p':
                os.system('cls')
                print()
                final_password = ''
                for i in range(password_length):
                    final_password += generate_random_char(choices)
                print(f'Your password is : {final_password}\n')
            elif ans == 'd':
                os.system('cls')
                print(f'\nGood luck. Your password is : {final_password}')
                break
        else: 
            print('Invalid input. Please try again!!!')

print(password_generator())