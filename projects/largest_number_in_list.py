# Largest Number in List
#
# Create a list of numbers.
# Find and display the largest number.
#
# Example:
# Numbers: [5, 8, 2, 15]
# Largest Number: 15

numbers = [5, 8, 1, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f'Largest Number: {largest}')