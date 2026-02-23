cart_prices = [1200, 2500, 1200, 800, 3000, 2500]

# Remove duplicates
unique_prices = list(set(cart_prices))

# Calculate total
total = sum(unique_prices)

# Apply 10% discount if total > 5000
if total > 5000:
    total *= 0.90

# Add 18% GST
total *= 1.18

print("Unique Prices:", unique_prices)
print("Final Payable Amount: ₹", round(total, 2))