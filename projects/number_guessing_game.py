# Number Guessing Game
#
# Generate a random number between 1 and 10.
# Ask the user to guess the number.
# Tell them if they guessed correctly.
#
# Example:
# Guess the number: 5
# Correct!

import random

random_number = random.randint(1, 10)
guessed_number = int(input('Guess The Number: '))

result = ''

if guessed_number == random_number:
    result = 'Correct'
elif guessed_number < random_number:
    result = 'Too low!'
else:
    result = 'Too high!'

print(f'Random Number: {random_number}')
print(f'Guess: {guessed_number}')
print(f'Result: {result}')
