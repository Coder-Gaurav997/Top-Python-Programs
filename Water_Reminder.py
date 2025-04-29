# Importing necessary modules
import time, datetime
from plyer import notification   

# Print welcome message
print("\nWELCOME TO WATER REMINDER")
print("-------------------------")
 
# Ask the user for the reminder interval in minutes
reminder_interval = int(input("\nEnter the reminder interval in minutes: "))

# Creating the reminder function
def remind_to_drink_water():
    notification.notify(
        title = "Hey There!",
        message = "It's Time To Drink Water",
        ticker = "Notification From Python")

while True:
    current_time = datetime.datetime.now()  # Get current system time
    if current_time.minute % reminder_interval == 0:  # Check if it's time for a reminder
        remind_to_drink_water()  # Call the reminder function
    time.sleep(60)  # Wait for 1 minute before checking again

# Author: GAURAV PANDEY