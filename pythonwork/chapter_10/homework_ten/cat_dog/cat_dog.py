from pathlib import Path

cat_dog = ['cats.txt', 'dogs.txt']

for cd in cat_dog:
    path = Path(cd)
    try:
        print(path.read_text(encoding='utf-8'))
    except FileNotFoundError:
        pass   #print(f"Sorry, the file {path} does not exist.")
