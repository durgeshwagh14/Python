def check_user_input_palindrome():
    user_string = input("Enter a word or phrase to check if it's a palindrome: ")
    
    # Remove spaces and convert to lowercase
    clean_string = user_string.replace(" ", "").lower()
    
    # Check for palindrome
    if clean_string == clean_string[::-1]:
        print(f"'{user_string}' is a palindrome! ✅")
    else:
        print(f"'{user_string}' is not a palindrome. ❌")

# Call the function
check_user_input_palindrome()
