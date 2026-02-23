# List of student marks
marks = [95, 67, 120, -5, 88, 76, 54, 100, 45]

# Remove invalid marks
valid_marks = [m for m in marks if 0 <= m <= 100]

# Calculate average
average = sum(valid_marks) / len(valid_marks)

# Find topper(s)
highest = max(valid_marks)
toppers = [m for m in valid_marks if m == highest]

# Grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

print("Valid Marks:", valid_marks)
print("Average:", round(average, 2))
print("Topper Marks:", toppers)
print("Overall Grade:", grade)