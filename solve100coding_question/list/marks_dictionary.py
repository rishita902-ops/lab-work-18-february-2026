# Create dictionary of student marks
marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88,
    "David": 95,
    "Eva": 90
}

# Find topper
topper = max(marks, key=marks.get)
highest_marks = marks[topper]

print("Topper:", topper)
print("Marks:", highest_marks)