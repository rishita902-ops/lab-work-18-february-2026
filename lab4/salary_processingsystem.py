salaries = [25000, 55000, 72000, 18000, 51000, 45000]
minimum_wage = 20000

# Remove salaries below minimum wage
valid_salaries = [s for s in salaries if s >= minimum_wage]

# Add 5% bonus to salary > 50000
for i in range(len(valid_salaries)):
    if valid_salaries[i] > 50000:
        valid_salaries[i] *= 1.05

# Sort descending
valid_salaries.sort(reverse=True)

# Top 3 highest salaries
top_3 = valid_salaries[:3]

print("Processed Salaries:", valid_salaries)
print("Top 3 Highest Salaries:", top_3)