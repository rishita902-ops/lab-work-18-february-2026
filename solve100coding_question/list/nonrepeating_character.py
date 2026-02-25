s = "swiss"
freq = {}

# Count characters
for char in s:
    freq[char] = freq.get(char, 0) + 1

# Find first non-repeating
for char in s:
    if freq[char] == 1:
        print(char)
        break