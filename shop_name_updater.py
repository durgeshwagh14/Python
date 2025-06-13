import math, random
import getpass

class Shop:
    def __init__(self):
        self.name = "Amul"

    def generate_OTP(self):
        OTP = ""
        for _ in range(6):
            OTP += str(random.randint(0, 9))
        return OTP

    def change_pass(self):
        no = input("Enter Your Mobile Number used in registered a shop :")
        otp = self.generate_OTP()
        print("Verify the Mobile Number Using OTP of 6 digits:", otp)

        user_otp = input("Enter the OTP: ")

        if user_otp == otp:
            print("✅ OTP Verified Successfully!")
            correct_password = "12345"

            new_name = input("Enter Shop new Name: ")
            password = getpass.getpass("Enter Your Password: ")
            if password == correct_password:
                self.name = new_name
                print(f"✅ Shop name changed successfully to: {self.name}")
            else:
                print("❌ Incorrect Password.")
        else:
            print("❌ OTP Verification Failed. Please try again.")

if __name__ == "__main__":
    n = Shop()
    n.change_pass()
