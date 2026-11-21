from pathlib import Path
import json

path = Path('love_numbers.json')

number = input("Please enter your favorite number:")
try:
    favorite_number = int(number)
except ValueError:
    # 用户输入的不是整数，就原样当文本存，程序不崩
    print(f"{number} is not a whole number, saving it as text.")
    favorite_number = number

contents = json.dumps(number)
path.write_text(contents, encoding='utf-8')
print(f"Saved {favorite_number} to {path}")