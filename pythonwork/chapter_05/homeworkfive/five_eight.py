# 以特殊方式跟管理员打招呼 * 处理没有用户的情形
user_names = []

if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print(f'Hello {user_name}, would you like to see a status report?')
        else:
            print(f'Hello {user_name.title()}, thank you for logging in again.')
else:
    print('We need find some users!')
    
# 检查用户名
print("")

current_users = ['Alice', 'Bob', 'Charlie', 'Diana', 'EVe']
new_users = ['alice', 'bob', 'frank', 'grace', 'henry']

current_users_copy = [users.lower() for users in current_users]
#current_users_copy = []
#for users in current_users:
    #current_users_copy.append(users.lower())

for new_user in new_users:
    if new_user in current_users_copy:
        print("Please enter different usernames.")
    else:
        print(f"{new_user} is available.")

# 序数
print('\nOrdinal numbers:')

ordinal_numbers = list(range(1,10))
print(ordinal_numbers)

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f'{ordinal_number}st')
    elif ordinal_number == 2:
        print(f'{ordinal_number}nd')
    elif ordinal_number == 3:
        print(f'{ordinal_number}rd')
    else:
        print(f'{ordinal_number}th')
