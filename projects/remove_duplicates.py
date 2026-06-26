# Remove Duplicates
#
# Create a list containing duplicate values.
# Remove duplicates.
# Display the new list.
#
# Example:
# Original: [1, 2, 2, 3]
# New: [1, 2, 3]

original = [1, 2, 2, 3]
new = [0]

print(len(new))


for index in range(0, len(original)):
    if new[index] == original[index]:
        original.pop(index)
    new.append(original[index])

new.pop(0)

print(f'New: {new}')