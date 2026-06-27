# To-Do List
#
# Allow the user to add tasks to a list.
# Display all tasks after adding them.
#
# Example:
# Add task: Learn Python
# Add task: Read Docs
#
# Tasks:
# 1. Learn Python
# 2. Read Docs

print('Todo List: ')
print(' - Write Done When You Are Done With Adding Todo')
print('')

is_running = 1
count = 0
todos = []

while is_running:
    todo = input('Add Task: ')
    if todo == 'done':
        is_running = 0
    else:
        todos.append(todo)

print('')
print('Tasks: ')

for todo in todos:
    count += 1
    print(f'{count}. {todo}')