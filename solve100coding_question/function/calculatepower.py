def power(base, exponent):
    # Base case: any number to the power 0 is 1
    if exponent == 0:
        return 1
    # Handle negative exponent
    elif exponent < 0:
        return 1 / power(base, -exponent)
    else:
        return base * power(base, exponent - 1)

# Example usage
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"{base}^{exponent} =", power(base, exponent))