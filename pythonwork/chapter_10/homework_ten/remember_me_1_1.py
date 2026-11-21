from pathlib import Path
import json

def get_stored_user_info(path):
    """如果储存了用户信息, 就获取他"""
    if path.exists():
        contents = path.read_text(encoding='utf-8')
        return json.loads(contents)
    else:
        return None

def get_new_user_info(path):
    """提示用户输入用户名, 及其另外两项信息"""
    username = input("What is your name?")
    occupation = input("What is your occupation?")
    year = input("What old are you?")

    user_info = {
        'username': username,
        'occupation': occupation,
        'year': year

    }

    contents = json.dumps(user_info)
    path.write_text(contents, encoding='utf-8')
    return user_info

def greet_user():
    """问候用户指出其名字"""
    path = Path('username_1_1.json')
    user_info = get_stored_user_info(path)
    if user_info:
        print(f"Welcome back, {user_info['username']}.\n"
              f"你是一名 {user_info['year']}岁的 {user_info['occupation']}.")
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info['username']}")

greet_user()