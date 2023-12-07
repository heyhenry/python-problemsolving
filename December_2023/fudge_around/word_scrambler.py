import random

user_input = input("Enter words to be scrambled into a single 'word': ")

temp_words = [w for w in user_input if w != ' ']
random.shuffle(temp_words)
word = ''
for w in temp_words:
    word += w

print(word)

