marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88,
    "David": 95
}

# Find key with maximum value
max_key = max(marks, key=marks.get)

print("Key with maximum value:", max_key)
print("Maximum value:", marks[max_key])