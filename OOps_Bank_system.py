import random
import string
import getpass

def generateOTP(length=6):
    characters = string.digits + string.ascii_uppercase + string.ascii_lowercase
    OTP = ''.join(random.choices(characters, k=length))
    return OTP

class Bank:
  def __init__(self):
    self.accounts = {}

class Account:
  def __init__(self, name, mobile, balance=0):
    self.name = name
    self.mobile = mobile
    self.balance = balance

  def credit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"✅ ₹{amount} credited successfully to {self.name}'s account.")
    else:
      print("❌ Credit amount must be positive.")

  def debit(self, amount):
    if amount > 0:
      if amount <= self.balance:
        self.balance -= amount
        print(f"✅ ₹{amount} debited successfully from {self.name}'s account.")
      else:
        print("❌ Insufficient balance!")
    else:
      print("❌ Debit amount must be positive.")

  def display_balance(self):
    print(f"💰 Current Balance for {self.name}: ₹{self.balance}")

def banking_menu(account):
    while True:
        account.display_balance()
        print("1. Credit (Deposit)")
        print("2. Debit (Withdraw)")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
                amount = int(input("Enter amount to credit: ₹"))
                account.credit(amount)
                # Removed the redundant invalid amount print which was always printing after the credit
        elif choice == '2':
                amount = int(input("Enter amount to debit: ₹"))
                account.debit(amount)
                # Removed the redundant invalid amount print which was always printing after the debit
        elif choice == '3':
            print("🙏 Thank you! Exiting...")
            break
        else:
            print("❌ Invalid option. Try again.")

# Main program

bank = Bank()

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

user_account = Account(name, mobile)
bank.accounts[mobile] = user_account


while True:
    print("\n🔐 Verify Your Account")
    print("1. Using PIN")
    print("2. Using OTP")

    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        pin = getpass.getpass("Enter your password: ")
        if pin == '1234':
            print("✅ PIN Verified Successfully!")
            banking_menu(user_account)
            break
        else:
            print("❌ Invalid PIN. Try again.")

    elif choice == '2':
        otp = generateOTP(6)
        print("📨 Your OTP is:", otp)
        user_otp = input("Enter the OTP: ")
        if user_otp == otp:
            print("✅ OTP Verified Successfully!")
            banking_menu(user_account)
            break
        else:
            print("❌ OTP Verification Failed. Try again.")

    else:
        print("❌ Invalid choice. Enter 1 or 2.")
