p = int(input("Enter principal: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))

ci =p * (1 + r/100) ** t - p
print("compound interest =", ci)
