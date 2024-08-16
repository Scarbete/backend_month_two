# Alias & import & from & libraries
from random import randint as generate_random_number
import emoji
from decouple import config

from termcolor import cprint
import calculator
from person import Person

print(generate_random_number(1, 5))

print(calculator.addition(8, 2))
print(calculator.multiplication(8, 2))

friend = Person(name='MaybeYato', age=20)
print(f'My friend - {friend}')
print('Test class', str(friend))

cprint(text='colored text', color='red', on_color='on_cyan')
print(emoji.emojize('Python is :thumbs_up:'))

db_url = config('DATABASE_URL')
print(db_url)

number = config('MY_NUMBER', cast=int)
print(number * 2)

commented_text = config('COMMENTED', default='commented_text')
print(commented_text)
