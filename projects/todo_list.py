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

task_1 = input('Add Task: ')
task_2 = input('Add Task: ')

tasks = [task_1, task_2]

print('')
print('Tasks: ')
print(f'1. {tasks[0]}')
print(f'2. {tasks[1]}')