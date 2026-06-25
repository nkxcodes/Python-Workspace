# Smallest Number in List
#
# Create a list of numbers.
# Find and display the smallest number.
#
# Example:
# Numbers: [5, 8, 2, 15]
# Smallest Number: 2

numbers = [5, 8, 2, 15]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(f'Smallest Number: {smallest}')