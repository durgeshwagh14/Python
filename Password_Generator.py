import random
import string

def generate_password(length=12):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine them into one pool
    all_chars = letters + digits + symbols

    # Randomly select characters
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Get length input from user
length = int(input("Enter password length: "))
print("Generated Password:", generate_password(length))
