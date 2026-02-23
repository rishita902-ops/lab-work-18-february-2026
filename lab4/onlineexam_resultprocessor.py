scores = [45, 32, 67, 29, 34, 50, 38]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks of 5 to those scoring between 30–35
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

print("Updated Scores:", scores)