def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Example usage
terms = int(input("Enter the number of terms: "))
print("Fibonacci series:", fibonacci_series(terms))