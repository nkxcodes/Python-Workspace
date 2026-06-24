# Even or Odd Checker
#
# Ask the user for a number.
# Determine whether it is even or odd.
# Display the result.
#
# Example:
# Enter number: 8
# 8 is Even

number = int(input('Enter Number: '))

if number % 2 == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')