#version1.0
alien_color = 'green'
if alien_color == 'green':
    print("The player scored five points.")

#version1.1
alien_color = 'red'
if alien_color == 'green':
    print("The player scored five points.")

#version2.0
print("\nVersion2.0")

alien_color = 'green'
if alien_color == 'green':
    print("The player scored five points.")
else:
    print("The player scored ten points.")

#version2.1
print("\nVersion2.1")

alien_color = 'red'
if alien_color == 'green':
    print("The player scored five points.")
else:
    print("The player scored ten points.")

#alien_color version3.0
print("\nVersion3.0")

alien_color = 'green'
if alien_color == 'green':
    print("The player scored five points.")
elif alien_color == 'yellow':
    print("The player scored ten points.")    
else:
    print("The player scored fifteen points.")

#alien_color version3.1
print("\nVersion3.1")

alien_color = 'yellow'
if alien_color == 'green':
    print("The player scored five points.")
elif alien_color == 'yellow':
    print("The player scored ten points.")    
else:
    print("The player scored fifteen points.")

#alien_color version3.2
print("\nVersion3.2")

alien_color = 'red'
if alien_color == 'green':
    print("The player scored five points.")
elif alien_color == 'yellow':
    print("The player scored ten points.")    
else:
    print("The player scored fifteen points.")

#Different stages of life    
print('')

age = 20
if age < 2:
    print('This perosn is a baby.')
elif age < 4:
    print('This person is a toddler.')
elif age < 13:
    print('This person is a child.')
elif age < 18:
    print('This person is a teenager.')
elif age < 65:
    print('This person is a young and middle-aged adult.')
else:
    print('This person is a old person.')

#liked fruits
print('')

favorite_fruits = ['apple', 'banana', 'pomelo',
                   'lychee', ]
if 'banana' in favorite_fruits:
    print('You really like bananas!')
if 'watermelon' in favorite_fruits:
    print('You really like watermelons!')
