class BankAccount:
    def __init__(self, account_number, holder_name, initial_balance):
        self.account_number = account_number       # Public
        self._holder_name = holder_name            # Protected
        self.__balance = initial_balance           # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def _display_holder(self):
        print(f"Account holder: {self._holder_name}")


# Subclass with limited access to parent class members
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, initial_balance, interest_rate):
        super().__init__(account_number, holder_name, initial_balance)
        self.interest_rate = interest_rate  # Public

    def apply_interest(self):
        interest = self.get_balance() * (self.interest_rate / 100)
        print(f"Applying interest: ₹{interest}")
        self.deposit(interest)

    def display_info(self):
        self._display_holder()  # Accessing protected method
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.get_balance()}")
        print(f"Interest Rate: {self.interest_rate}%")


# --- Usage Example ---
acc = SavingsAccount("1234567890", "Amit Verma", 10000, 4.5)
acc.display_info()
acc.deposit(5000)
acc.withdraw(3000)
acc.apply_interest()

# Trying to access private attribute directly (not recommended)
# print(acc.__balance)  # Will raise an error

# Accessing private variable using name mangling (not recommended)
print("Accessing private balance using name mangling:", acc._BankAccount__balance)
