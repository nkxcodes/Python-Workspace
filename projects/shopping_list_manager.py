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

item_1 = input('Add Item: ')
item_2 = input('Add Item: ')

shopping_list = [item_1, item_2]

print('')
print('Shopping List: ')
print(shopping_list[0])
print(shopping_list[1])