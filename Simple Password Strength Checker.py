import re

def check_password_strength(password):
    if len(password) < 6:
        return "🔴 Weak: Too short, minimum 6 characters required."

    if not re.search(r"[A-Z]", password):
        return "🟠 Weak: Add at least one uppercase letter."

    if not re.search(r"[a-z]", password):
        return "🟠 Weak: Add at least one lowercase letter."

    if not re.search(r"[0-9]", password):
        return "🟠 Weak: Add at least one number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "🟠 Weak: Add at least one special character (!@#$%^&*...)."

    return "✅ Strong Password!"

# Example run
password = input("🔐 Enter your password to check strength: ")
strength = check_password_strength(password)
print(strength)
