import random

import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

digits = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!#$%&*+-=?@^_'

pwd_length, pwd_digits, pwd_uppercase, pwd_lowercase, pwd_punctuation = 0, '0', '0', '0', '0'

def in_length():
    global pwd_length
    try:
        pwd_length = int(input('Enter password length: '))
    except ValueError:
        print('You enter NOT numbers. Use only numbers!')
        in_length()

def FAILcheck_yn(variable):
    if not((variable == 'y') or (variable == 'n')):
        print('Use ONLY "y" or "n"!')
        print_yn()
        return True

def print_yn():
    global pwd_digits, pwd_uppercase, pwd_lowercase, pwd_punctuation
    pwd_digits = input('Include numbers (yes = y, no = n): ')
    if FAILcheck_yn(pwd_digits): return
    pwd_uppercase = input('Include uppercase letters (yes = y, no = n): ')
    if FAILcheck_yn(pwd_uppercase): return
    pwd_lowercase = input('Include lowercase letters (yes = y, no = n): ')
    if FAILcheck_yn(pwd_lowercase): return
    pwd_punctuation = input('Include symbols "!#$%&*+-=?@^_"? (yes = y, no = n): ')
    if FAILcheck_yn(pwd_punctuation): return
    if all([pwd_digits == 'n', pwd_uppercase == 'n', pwd_lowercase == 'n', pwd_punctuation == 'n']):
        print("You didn't select any options. Choose at least one option!")
        print_yn()

in_length()
print_yn()

vocabular = ''

if pwd_digits == 'y':
    vocabular += digits
if pwd_uppercase == 'y':
    vocabular += uppercase
if pwd_lowercase == 'y':
    vocabular += lowercase
if pwd_punctuation == 'y':
    vocabular += punctuation

# print(vocabular) /to see all available symbols

s = ''
for i in range(pwd_length):
    s += random.choice(vocabular)
print("\033[32m {}" .format('Your password:'), s)
print("\033[37m\033[41m {} \033[0m" .format('Remember it!'))
