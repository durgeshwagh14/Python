numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num_str = input(f"Enter number {i+1}: ")
    num = int(num_str)
    numbers.append(num)

even_numbers = []

odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("\nAll entered numbers:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
