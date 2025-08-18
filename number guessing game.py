import random

def number_guessing_game():
    
    # Print a welcome message for the player.
    print("=======================================")
    print("   Welcome to the Number Guessing Game!  ")
    print("=======================================")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")

    # The computer picks a random whole number from 1 to 100 and stores it.
    secret_number = random.randint(1, 100)
    
    # Create a counter to keep track of how many guesses the player makes.
    attempts = 0

    # This loop will run forever until we tell it to stop (with 'break').
    while True:
        # Ask the player to type their guess and store it as text.
        guess_str = input("Enter your guess: ")
        
        # Check if the text the user entered contains only digits (like "50").
        if guess_str.isdigit():
            # If it's a valid number, turn the text into an actual number for math.
            guess = int(guess_str)
            
            # Add 1 to the attempts counter since this was a valid guess.
            attempts = attempts + 1

            # --- Compare the player's guess to the secret number ---
            
            # If the guess is too small, give a hint.
            if guess < secret_number:
                print("Too low! Try a higher number.")
                
            # If the guess is too big, give a hint.
            elif guess > secret_number:
                print("Too high! Try a lower number.")
                
            # If the guess is not too high or too low, it must be correct!
            else:
                # Print a success message.
                print(f"\n🎉 Congratulations! You guessed the number!")
                print(f"It took you {attempts} attempts.")
                
                # 'break' stops the 'while' loop and ends the game.
                break  
        else:
            # This part runs if the user typed something that wasn't a number (like "hello").
            print("That's not a valid number! Please try again.")

# This line is a standard way to start the program by calling our main function.
if __name__ == "__main__":
    number_guessing_game()
