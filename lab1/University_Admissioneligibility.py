marks = float(input("Enter 12th percentage:"))
maths = input("Did you study Mathematics? (yes/no):").lower()
entrance = int(input("Enter enterance exam score:"))
if marks < 75:
     print("Not eligible: Less than 75% in 12th")
elif maths !="yes":
       print("Not eligible: Mathematics not studied")
elif entrance < 80:
       print("Not eligible: Enterance score below 80:")
else:
       print("Congratulatios! You are eligible for admission")
             