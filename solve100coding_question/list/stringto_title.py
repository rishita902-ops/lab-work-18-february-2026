s = "python is fun and easy to learn"
words = s.split()  # split into words
title_words = []

for word in words:
    if word:  # check if word is not empty
        title_word = word[0].upper() + word[1:].lower()
        title_words.append(title_word)

title_case = ' '.join(title_words)
print(title_case)