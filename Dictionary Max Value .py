data = {"a": 1, "b": 2, "c": 3, "d": 3}

# Find the maximum value in a single pass
max_value = max(data.values())

# Use a list comprehension to find all keys with that maximum value
keys_with_max_value = [key for key, value in data.items() if value == max_value]

print(keys_with_max_value)
