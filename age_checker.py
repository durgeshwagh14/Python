from datetime  import datetime

name = input("Enter your name : ")
def age(year):
  n = int(input("Enter DOB year : "))
  current_year = datetime.now().year
  return current_year - n

a = age(name)
print(f"{name} Age is {a}")
