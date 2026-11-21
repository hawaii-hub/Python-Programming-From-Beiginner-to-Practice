from pathlib import Path
import json

def get_stored_number(path):
    """如果储存了数字， 就获取它"""
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None
    
def get_new_number(path):
    """提示用户输入数字"""
    number = input("What is your favorite number.")
    contents = json.dumps(number)
    path.write_text(contents)
    return number

def favorite_number():
    """指出喜欢的数字"""
    path = Path('remember_numbers.json')
    number = get_stored_number(path)
    if number:
        print(f"I know your favorite number! It's {number}")
    else:
        number = get_new_number(path)
        print("We'll remember your favorite number!")

favorite_number()
