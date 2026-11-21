from pathlib import Path
import json

path = Path('love_numbers.json')
contents = path.read_text()
number = json.loads(contents)

print(number)