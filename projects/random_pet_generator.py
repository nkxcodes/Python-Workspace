
# Random Pet Generator

# Description
# Create a fun program that generates a random pet by combining a random color and a random animal.
# Example:
# Your pet is a Blue Rabbit!

import random

animals = ['Dog', 'Cat', 'Rabbit']
colors = ['Red', 'Blue', 'Green']

random_animal = random.choice(animals)
random_color = random.choice(colors)

print(f'Your pet is a {random_color} {random_animal}')