stock = [0, 5, 12, 8, 20, 3]

stock = [s for s in stock if s > 0]

for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

print("Total Inventory:", sum(stock))
print("Updated Stock:", stock)