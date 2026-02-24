n = int(input("Enter number: "))
i = 1
total = 0

while i <= n:
    if i % 2 == 0:
        total += i
    i += 1

print("Sum of even numbers =", total)    