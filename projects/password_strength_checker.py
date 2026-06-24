# Password Strength Checker
#
# Ask the user for a password.
# Check its length.
# Short passwords are Weak.
# Longer passwords are Strong.
#
# Example:
# Enter password: hello123
# Password Strength: Strong

print('Welcome to Password Strength Checker')

password = input('Enter Password: ')
password_strength = ''
length = len(password)

if length <= 6:
    password_strength = 'Very Weak'
elif length <= 8:
    password_strength = 'Weak'
elif length <= 11:
    password_strength = 'Moderate'
elif length <= 15:
    password_strength = 'Strong'
else:
    password_strength = 'Very Strong'

print(f'Password Strength: {password_strength}')