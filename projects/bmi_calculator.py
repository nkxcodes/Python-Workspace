# BMI Calculator
#
# Ask the user for weight in kilograms.
# Ask for height in meters.
# Calculate BMI using:
# BMI = weight / (height * height)
# Display the BMI.
#
# Example:
# Weight: 70
# Height: 1.75
# BMI: 22.86

weight = float(input('Enter Weight(kg): '))
height = float(input('Enter Height(m): '))

if weight == 0 or height == 0:
    print('Values cannot be zero')
else: 
    BMI = weight / (height * height)
    print(f'Weight: {weight}')
    print(f'Height: {height}')
    print(f'BMI: {round(BMI, 2)}')