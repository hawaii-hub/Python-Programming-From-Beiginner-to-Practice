#1 检查相等
car = 'subaru'

print(car)

print("Is car == 'subaru'? I predict Ture.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


#2 检查相等忽略大小写
print('')
car = 'Subaru'

print(car)

print("Is car.lower() == 'subaru'? I predict Ture.")
print(car.lower() == 'subaru')

print("\nIs car == 'subaru'? I predict False.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#3 检查不等
print('')

magician = 'alice'
print(magician)

print("Is magician != 'david'? I predict Ture.")
print(magician != 'david')

print("\nIs magician != 'alice'? I predict False.")
print(magician != 'alice')

#4 数值比较
print('')

age = 18
print(f"age = {age}")

print("Is age >= 17? I predict Ture.")
print(age >= 17)

print("\nIs age <= 10? I predict False.")
print(age <= 10)

#5 检查多个条件

#5.1 and
print('')

age_1 = 22
age_2 = 24

print("Is age_1 >= 21 and age_2 >= 17? I predict Ture.")
print(age_1 >= 21 and age_2 >= 17)

print("\nIs age_1 >= 21 and age_2 <= 17? I predict False.")
print(age_1 >= 21 and age_2 <= 17)

#5.2 or

print("\nIs age_1 >= 21 or age_2 <= 17? I predict False.")
print(age_1 >= 21 or age_2 <= 17)

print("\nIs age_1 <= 21 or age_2 <= 17? I predict False.")
print(age_1 <= 21 or age_2 <= 17)

#6 检查特定值是否在列表中

print('')

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print("\nThe 'mushroos' in ruquested_toppings? I predict Ture.")
print('mushrooms' in requested_toppings)

print("\nThe 'pepperoni' in ruquested_toppings? I predict False.")
print('pepperoni' in requested_toppings)

#7 检查特定值是否不在列表中

print('')

banned_users = ['andrew', 'carokina', 'david']

print("\nThe 'mushroos' not in banned_users? I predict Ture.")
print('mushrooms' not in banned_users)