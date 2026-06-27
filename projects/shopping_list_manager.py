# Shopping List Manager
#
# Allow the user to add items to a shopping list.
# Display all items.
#
# Example:
# Add item: Milk
# Add item: Bread
#
# Shopping List:
# Milk
# Bread

print('Shopping List Manager: ')
print(' - Write Done When You Are Done With Adding Items')
print('')

is_running = 1
count = 0
shopping_list = []

while is_running:
    item = input('Add Item: ')
    if item == 'done':
        is_running = 0
    else:
        shopping_list.append(item)

print('')
print('Shopping List: ')

for item in shopping_list:
    count += 1
    print(f'{count}. {item}')