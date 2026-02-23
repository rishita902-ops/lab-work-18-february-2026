attendance = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]

# Calculate attendance percentage
percentage = (sum(attendance) / len(attendance)) * 100

# Identify below 75%
status = "Below 75%" if percentage < 75 else "Eligible"

# Replace consecutive absences with warning flag (-1)
for i in range(len(attendance) - 1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = -1
        attendance[i+1] = -1

print("Attendance %:", round(percentage, 2))
print("Status:", status)
print("Updated Attendance:", attendance)