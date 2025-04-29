# Importing the necessary modules
import secrets
import string

# Function to generate a password of a specified length
def generate_password(length):
    # Define the set of characters to choose from for the password
    characters = (string.ascii_letters + string.digits + string.punctuation)
    # Generate the password by randomly choosing characters from the set
    password = ''.join(secrets.choice(characters) for _ in range(length))
    # Print the generated password
    print(f"Generated Password : {password}\n")

def main():
    # Run an infinite loop
    while True:
        try:  
            # Prompt the user to enter the length of the password
            length = int(input("Enter The Length Of The Password : "))
            # Validate the length given by the user
            if length < 1 or length > 15:
                print("-- PLEASE ENTER THE LENGTH B/W 1 - 15 ONLY --\n")
                continue
            # Generate and print a password of the specified length
            generate_password(length)
        except KeyboardInterrupt:  # Handling 'KeyboardInterrupt' error
            print("\n-- EXITING THE PROGRAM --\n")
            exit()
        except Exception:  # Handling all other possible errors
            print("-- ERROR! ENTER LENGTH IN 'INTEGERS' ONLY --\n")    

if __name__ == "__main__":  
    # Print the title of the program
    print("\nPASSWORD GENERATOR")
    print("------------------")
    main()  # Calling the main function

# Author: GAURAV PANDEY       