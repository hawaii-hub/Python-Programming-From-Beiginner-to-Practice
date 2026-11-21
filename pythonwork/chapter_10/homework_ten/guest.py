from pathlib import Path

contents = input("Please enter your name: ")

path = Path('fuest.txt')
path.write_text(contents)