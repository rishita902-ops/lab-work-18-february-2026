transactions = [5000, -2000, 15000, -5000, 12000, -3000]

balance = sum(transactions)

withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals)

large_deposits = len([t for t in transactions if t > 10000])

print("Final Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", large_deposits)