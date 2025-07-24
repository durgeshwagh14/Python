items_price = {
    "Apple": 30,
    "Banana": 10,
    "Milk": 45,
    "Bread": 40,
    "Eggs": 60,
    "Rice (1kg)": 55,
    "Soap": 25,
    "Shampoo": 120,
    "Toothpaste": 35,
    "Oil (1L)": 150
}

total_price = 0
while True:
  item = input("Enter the item you want (or type 'done' to finish): ")
  if item.lower() == 'done':
    break

  if item in items_price:
    total_price += items_price[item]
    print(f"Added {item}. Current total: {total_price}")
  else:
    print(f"Sorry, {item} is not in stock.")

print(f"\nYour total bill is: {total_price}")
