cart =float(input("Enter cart value:"))
membership =input("Enter membership(silver/gold/platinum):").lower()
festival =input("Festival season?(yes/no)").lower()
discount = 0
if membership == "silver":
    discount = 5
elif membership == "gold":
      discount = 10
elif membership == "platinum":
       discount = 15
if festival == "yes":
        discount = max(discount,20)
        final_amount = cart - (cart * discount / 100)
        print("Discount applied:", discount, "%")
        print("Final payable amount:", final_amount)                   
                  