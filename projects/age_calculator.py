# Project: Age Calculator
#
# Description:
# This program calculates a person's age based on their birth year.
# The user enters their birth year, and the program determines
# their current age by subtracting the birth year from the current year.
#
# Concepts Practiced:
# - Variables
# - User Input
# - Data Type Conversion (int)
# - Arithmetic Operations
# - Output Formatting
#
# Example:
# Enter your birth year: 2005
# Your age is 21 years.
#
# Goal:
# To understand how to take input from the user, perform calculations,
# store values in variables, and display the result in a meaningful way.

user_birth_year = input('Enter Your Birth Year: ')
current_year = 2026

if user_birth_year == '':
    print('Invalid Birth Year!')
else:
    user_birth_year = int(user_birth_year)

if user_birth_year >= current_year:
    print('Invalid Birth Year!')    
else:
    age = current_year - int(user_birth_year)
    print(f'Your Age Is {age} Years.')