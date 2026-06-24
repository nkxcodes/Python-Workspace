# Project: Simple Calculator
#
# Description:
# This program performs basic arithmetic operations on two numbers.
# The user enters two numbers and selects an operation
# (addition, subtraction, multiplication, or division).
# The program then calculates and displays the result.
#
# Concepts Practiced:
# - Variables
# - User Input
# - Data Type Conversion (int/float)
# - Arithmetic Operators (+, -, *, /)
# - Conditional Statements (if/elif/else)
# - Output Formatting
#
# Example:
# Enter first number: 10
# Enter second number: 5
# Choose operation (+, -, *, /): *
#
# Result: 50
#
# Goal:
# To understand how to take multiple inputs, perform calculations
# based on user choices, and display the output in a clear format.

first_number = int(input('Enter First Number: '))
second_number = int(input('Enter Second Number: '))
operation = input('Choose Opeartion (+, -, *, /): ')
result = 0

if operation == '+':
    result = first_number + second_number
    print(f'Result: {result}')
elif operation == '-':
    result = first_number - second_number
    print(f'Result: {result}')
elif operation == '*':
    result = first_number * second_number
    print(f'Result: {result}')
elif operation == '/':
    if second_number == 0:
        print('Cannot Divide By Zero')
    else:
        result = first_number / second_number
        print(f'Result: {result}')
else:
    print('Invalid Operation')