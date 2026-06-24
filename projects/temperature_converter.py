# Project: Temperature Converter
#
# Description:
# This program converts temperature values between different units.
# The user enters a temperature and chooses the conversion type
# (Celsius to Fahrenheit or Fahrenheit to Celsius).
# The program then calculates and displays the converted temperature.
#
# Concepts Practiced:
# - Variables
# - User Input
# - Data Type Conversion (int/float)
# - Arithmetic Operations
# - Conditional Statements (if/elif/else)
# - Output Formatting
#
# Example:
# Enter temperature: 25
# Choose conversion (C/F): C
#
# Result: 25°C = 77°F
#
# Goal:
# To understand how to take user input, apply mathematical formulas,
# use conditional logic, and display formatted results.
#
# Formulas:
# Celsius to Fahrenheit:
# F = (C × 9/5) + 32
#
# Fahrenheit to Celsius:
# C = (F - 32) × 5/9

temperature = int(input('Enter Temperature: '))
conversion = input('Enter Conversion (C/F): ')

if conversion == 'C':
    F = (temperature * 9/5 + 32)
    print(f'Result: {temperature}°{conversion} = {F}°F')
elif conversion == 'F':
    C = (temperature - 32) * 5/9
    print(f'Result: {temperature}°{conversion} = {C}°C')
else:
    print('Invalid Conversion!')