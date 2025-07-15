income_str = input("Enter Your Income :")
bill = float(input("Enter Your Bill :"))
discount = 0

if income < 0:
    print("Invalid Input: Income cannot be negative.")
elif  1000 <= income <= 14000:
    print(f"Your income is {income}😒, The Discount is Not Avaliable ")
elif  15000 <= income <= 20000:
    discount = 0.10
    print(f"Your income is {income}😁, The Discount is 10% ")
elif 20000 < income <= 50000:
    discount = 0.20
    print(f"Your income is {income}😊, The Discount is 20% ")
elif 50000 < income <= 70000:
    discount = 0.30
    print(f"Your income is {income}✅, The Discount is 30% ")
elif income >= 85000:
    discount = 0.40
    print(f"Your income is {income}🏆, The Discount is 40% ")
else :
  print("Invalid Input")

total_discount_bill = bill * discount
print(f"The total discount on your bill is: {total_discount_bill}")
final_bill = bill - total_discount_bill
print(f"Your final bill after discount is: {final_bill}")


'''
Enter Your Income :20000
Enter Your Bill :20000
Your income is 15000😁, The Discount is 10% 
The total discount on your bill is: 2000.0
Your final bill after discount is: 18000.0
'''
