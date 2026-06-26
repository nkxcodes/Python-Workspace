
import random

question = input('Ask a Question: ')

answers = ['Yes', 'No', 'Maybe', 'Ask again later']

random_answer = random.choice(answers)

print(f'Answer: {random_answer}')