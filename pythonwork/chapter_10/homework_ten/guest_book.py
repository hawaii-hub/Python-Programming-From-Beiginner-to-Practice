from pathlib import Path

path = Path('guest_book.txt')

book = ''
while True:
    contents = input("Please enter your name(or 'quit' to exit): ")

    if contents == 'quit':
        break
    else:
        book += contents + '\n'

path.write_text(book)