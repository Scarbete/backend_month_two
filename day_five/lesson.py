# Alias & import & from & libraries
from random import randint as generate_random_number
from termcolor import cprint
from person import Person
import calculator
import emoji

print(generate_random_number(1, 5))

print(calculator.addition(8, 2))
print(calculator.multiplication(8, 2))


friend = Person(name='MaybeYato', age=20)
print(f'My friend - {friend}')
print('Test class', str(friend))

cprint(text='colored text', color='red', on_color='on_cyan')
print(emoji.emojize('Python is :thumbs_up:'))
