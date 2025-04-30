# Importing necessary modules
import time, datetime
from plyer import notification

# Creating the notifier function
def desktop_notifier():
    notification.notify(
    title = "Hey There!",
    message = "It's Time To Take Some Rest",
    ticker = "Notification From Python")

# Print welcome message
print("\nWELCOME TO DESKTOP NOTIFIER")
print("---------------------------")

# Main function to run the program
def main():
    # Ask the user for the notifier interval in minutes
    notifier_interval = int(input("Enter the notifier interval in minutes: "))

    while True:
        current_time = datetime.datetime.now()  # Get current system time
        if current_time.minute % notifier_interval == 0:  # Check if it's time for a notification
            desktop_notifier()  # Call the notifier function
            print("\n-- Notification Has Been Delivered --")

        time.sleep(60)  # Wait for 1 minute before checking again

if __name__ == "__main__":
    main()  # Call the main function

# Author: GAURAV PANDEY