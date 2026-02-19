amount =float(input("Enter transaction amount:"))
months =int(input("Enter account age(in months):"))
international =input("Is transaction international?(yes/no):").lower()
if amount > 200000 and months < 6 and international == "yes":
    print("Transaction FLAGGED for manual verification")
else:
    print("Transaction is normal")