
print('Welcome To Student Todo Tracker')

user_name = input('Enter Your Name: ')
user_class = input('Enter Your Class: ')

is_running = 1
count = 0
student_todos = []

print('')
print(user_name + ' ' + user_class)
print('')

while is_running:
    todo = input('Add a Task: ')
    if todo == 'done':
        is_running = 0
    else: 
        student_todos.append(todo)

print('')
print('Your Tasks: ')

for todo in student_todos:
    count += 1
    print(f'{count}. {todo}')