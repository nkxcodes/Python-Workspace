# Positive, Negative, or Zero
#
# Ask the user for a number.
# Check whether it is positive, negative, or zero.
# Display the result.
#
# Example:
# Enter number: -5
# Number is Negative

number = int(input('Enter Number: '))
result = ''

if number > 0:
    result = 'Positive'
elif number < 0:
    result = 'Negative'
else:
    result = 'Zero'

print(f'Number is {result}')
