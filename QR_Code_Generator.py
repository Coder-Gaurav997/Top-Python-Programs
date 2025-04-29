# Import the qrcode library to generate QR codes
import qrcode as qr

# Function to generate a QR code from a given link and save it as an image
def qrcode_generator(link, filename):
    try:
        # Create a QR code object from the given link
        img = qr.make(link)        
        # Save the QR code image to the specified filename
        img.save(filename)
        
        # Print a success message with the filename
        print(f"\n-- QR code saved as {filename} --\n")
    except ValueError or TypeError:
        print("\n-- Error! Please enter a valid link or filename --\n")            
    except Exception as e:
        # Print an error message if any exception occurs
        print(f"\n-- An error occurred: {e} --\n")

# Introduction of QR Code
print("\nQR CODE GENERATOR")
print("-----------------")

# Main function to handle user input and generate the QR code
def main():    
    # Prompt the user to enter the link to make its QR code
    link = input("Enter the link to make its QR code: ")    
    # Prompt the user to enter the filename for the QR code (default: QR Code.png)
    filename = input("Enter the filename for the QR code [Default: QR_Code.png]: ")
    
    # If the user doesn't enter a filename, use the default filename
    if not filename:
        filename = "QR Code.png"    
    # If the filename doesn't end with '.png', append '.png' to it
    if not filename.endswith(".png"):
        filename += ".png"
    
    # Call the qrcode_generator function with the user's input
    qrcode_generator(link, filename)

# Check if the script is being run directly (not being imported)
if __name__ == "__main__":
    # Call the main function to start the program
    main()

# Author: GAURAV PANDEY