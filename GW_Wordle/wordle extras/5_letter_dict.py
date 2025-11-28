import os
import random

def load_word_list(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, filename)

    with open(filepath, "r") as file:
        raw_words = [line.strip().upper() for line in file]

    clean_words = [
        word for word in raw_words
        if len(word) == 5 and word.isalpha()
    ]

    return clean_words

words = load_word_list("allowed_words.txt")

print(len(words))
for word in words:
    print(word, end = " ")