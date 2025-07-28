import random
import string

balance = 1000

def generateOTP(length=6):
    characters = string.digits + string.ascii_uppercase + string.ascii_lowercase
    OTP = ''.join(random.choices(characters, k=length))
    return OTP

def credit():
    global balance
    amount = int(input("Enter amount to credit: ₹"))
    balance += amount
    print(f"✅ ₹{amount} credited successfully.")

def debit():
    global balance
    amount = int(input("Enter amount to debit: ₹"))
    if amount <= balance:
        balance -= amount
        print(f"✅ ₹{amount} debited successfully.")
    else:
        print("❌ Insufficient balance!")

def banking_menu():
    while True:
        print(f"\n💰 Current Balance: ₹{balance}")
        print("1. Credit (Deposit)")
        print("2. Debit (Withdraw)")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            credit()
        elif choice == '2':
            debit()
        elif choice == '3':
            print("🙏 Thank you! Exiting...")
            break
        else:
            print("❌ Invalid option. Try again.")

# --- Main program ---

name = input("Enter your name: ")
if  name.isalpha():
    print("👋 Hello", name)
else:
    print("enter valid name")
    exit()
mobile = input("Enter your mobile number: ")
if mobile.isdigit() and len(mobile)==10:
    print("📱 Your mobile number is", mobile)
else:
    print("Enter valid number")
    exit()

while True:
    print("\n🔐 Verify Your Account")
    print("1. Using PIN")
    print("2. Using OTP")

    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        pin = input("Enter your 4-digit PIN: ")
        if pin == '1234':
            print("✅ PIN Verified Successfully!")
            banking_menu()
            break
        else:
            print("❌ Invalid PIN. Try again.")

    elif choice == '2':
        otp = generateOTP(6)
        print("📨 Your OTP is:", otp)  # Simulate OTP send
        user_otp = input("Enter the OTP: ")
        if user_otp == otp:
            print("✅ OTP Verified Successfully!")
            banking_menu()
            break
        else:
            print("❌ OTP Verification Failed. Try again.")

    else:
        print("❌ Invalid choice. Enter 1 or 2.")
