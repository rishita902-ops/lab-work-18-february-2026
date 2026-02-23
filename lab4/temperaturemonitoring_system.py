temps = [35, 42, 38, 46, 30, 41, 44]

print("Hottest:", max(temps))
print("Coldest:", min(temps))

extreme_days = len([t for t in temps if t > 40])

for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"

print("Extreme Days (>40):", extreme_days)
print("Updated Temps:", temps)