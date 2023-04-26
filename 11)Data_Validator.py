# bad solution for website()
import re
import validators


def email():
    ma = re.match('[a-zA-Z0-9-._]+@[a-zA-Z].[a-z]', val)
    if ma is not None:
        print('Valid email address')
    else:
        print("Invalid email address")


def website():
    m = re.match('^https://[a-z](.*)\.(.*)\.[a-z]/?(.*)', val)
    n = re.match('^www\.(.*)\.[a-z]/?(.*)', val)
    if m is not None or n is not None:
        print('Valid URL')
    else:
        print('Invalid URL')
    #if validators.url(val):print('Valid URL')
    #else:print('Invalid URL')

def date():
    repl = val.replace('.', ' ').replace(',', ' ').replace('/', ' ')
    ls = repl.split()
    try:
        for i in range(len(ls)):
            ls[i] = int(ls[i])
    except ValueError:
        print('non number value fount')
    else:
        print(ls)
        if (ls[2] > 0 and len(str(ls[2])) <= 4 and ls[1] in [1, 3, 5, 7, 8, 10, 12] and 1 <= ls[0] <= 31) or (
                ls[2] > 0 and len(str(ls[2])) <= 4 and ls[1] in [4, 6, 9, 11] and 1 <= ls[0] <= 30) or (
                ls[2] > 0 and len(str(ls[2])) <= 4 and ls[1] == 2 and 1 <= ls[0] <= 28):
            print('Valid date')
        else:
            print('Invalid date')


def number():
    if val.isdigit() and int(val) >= 0:
        print('Valid Number')
    else:
        print('Invalid Number')


def card():
    num = val.replace(' ', '')
    if len(num) == 16 and num.isdigit():
        print("Valid credit card number")
    else:
        print('Invalid credit card number')


def phone():
    ph_num = val.replace(' ', '')
    if (ph_num.startswith('+374') and len(ph_num) == 12 and ph_num[1:].isdigit()) or (
            ph_num.startswith('0') and len(ph_num) == 9 and ph_num.isdigit()):
        print('Valid phone number')
    else:
        print('Invalid phone number')


while True:
    print(
        'Here are 6 types of data for checking, please choose one of the options: \n1 - Email\n2 - Website URL\n3 - '
        'Date\n4 - Number\n5 - Credit Card Number\n6 - Mobile Phone Number\n7 - For ending program\n ')
    choice = input("Your option: ")
    val = input('Enter your value for checking: ')
    if choice == '1':
        email()
    elif choice == '2':
        website()
    elif choice == '3':
        date()
    elif choice == '4':
        number()
    elif choice == '5':
        card()
    elif choice == '6':
        phone()
    elif choice == '7':
        print('Program ended!')
        break
    else:
        print('Please type only one of these numbers. ')
