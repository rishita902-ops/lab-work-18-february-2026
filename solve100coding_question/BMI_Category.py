weight = int(input("Enter weight(kg): "))
height = int(input("Enter height(m): "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normalweight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")