sentence = "Python is fun and easy to learn"
words = sentence.split()
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)