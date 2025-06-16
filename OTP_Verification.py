import math,random

def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


if __name__ == "__main__":
  otp = generateOTP()
  print("OTP of 4 digits:", otp)
  user_otp = input("Enter the OTP: ")
  if user_otp == otp:
    print("✅ OTP Verified Successfully!")
  else:
    print("❌ OTP Verification Failed. Please try again.")

