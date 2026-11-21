from pathlib import Path

contents = "I love progaming.\n"
contents += "I love creating new gasmes.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)