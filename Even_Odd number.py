user = int(input("How many number you want to enter ?"))

even_number=[]
odd_number=[]

for i in range(user):
  num = int(input(f"Enter a number {i+1} :"))

  if num % 2 == 0:
    even_number.append(num)
  else:
    odd_number.append(num)

print()
print("The Even Number is :",*even_number)
print("The Sum of Even Number is : ",sum(even_number))
even_number.sort()
print("The Even Number Sort in Acending Order :",*even_number)
print()
print("The odd Number is : ",*odd_number)
print("The Sum of Odd Number is : ",sum(odd_number))
odd_number.sort()
print("The Odd Number Sort in Acending Order :",*odd_number)
print()
print("The Even count is :",len(even_number))
print("The Odd count is :",len(odd_number))
