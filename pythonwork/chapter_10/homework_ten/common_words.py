from pathlib import Path

def count_words(path, word):
    """计算一个单词出现的次数"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.lower().split()
        num_words = words.count(word.lower())
        print(f"The word '{word}' appears about {num_words} times in {path}.")

path = Path('alice.txt')
count_words(path, 'the')  