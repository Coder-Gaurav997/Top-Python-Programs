# Import the random module 
from random import randint

# Print welcome message
print("\nWELCOME TO 'GUESS THE NUMBER' GAME")
print("-----------------------------------") 
print("RULE: GUESS THE NUMBER B/W 1 - 100\n")

user_guess = None  # Initialize the user's guess to None
guesses = 0  # Initialize the number of guesses to 0

num = randint(1, 100)  # Generate a random number between 1 and 100

while user_guess != num:  # Continue the game until the user guesses the correct number
    user_guess = int(input("\nGuess The Number: "))  # Get the user's guess

    if user_guess > 100 or user_guess < 1:  # Check if the user's guess is out of range (1-100) 
        print(f"-- YOU CAN ONLY ENTER NUMBER B/W 1 - 100!!! BUT YOU HAVE ENTERED {user_guess} --  ") 
     
    guesses += 1  # Increment the number of guesses    

    if user_guess > num:  # Check if the user's guess is greater than the correct number
        print("THIS NUMBER IS GREATER!!! TRY A SMALLER ONE\n")  

    elif user_guess < num:  # Check if the user's guess is smaller tshan the correct number
        print("THIS NUMBER IS SMALLER!!! TRY A GREATER ONE\n") 

    else:   
        print("--- CONGRATULATIONS! YOU WON ---")  # Print a winning message

print(f"YOU GUESS THE CORRECT NUMBER IN '{guesses}' ATTEMPTS\n")  # Print the number of attempts it took to win

# Author: GAURAV PANDEY