import random

# Example user input
names = ["Alice", "Bob", "Carol"]
numbers = [random.randint(1, 100) for _ in range(len(names))]

# Matching names to numbers
matches = dict(zip(names, numbers))

# Counting entries
num_names = len(names)
num_numbers = len(numbers)

print("Number of names entered:", num_names)
print("Number of numbers used:", num_numbers)
print("Matched cases:", matches)
