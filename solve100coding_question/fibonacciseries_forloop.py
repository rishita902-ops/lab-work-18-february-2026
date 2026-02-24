# Fibonacci series using for loop

n = int(input("Enter the number of terms: "))

a = 0
b = 1

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    print(a)
    print(b)
    
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c