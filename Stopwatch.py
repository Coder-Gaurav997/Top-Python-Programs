import time

# Define a function to simulate a stopwatch
def stopwatch():
    second = 0  # Initialize the second counter
    while True:        
        # Calculate minutes and seconds using divmod
        mins, secs = divmod(second, 60)
        # Format the time as MM:SS
        stopwatch = "{:02d}:{:02d}".format(mins, secs)
        # Print the time and overwrite the previous line
        print(stopwatch, end='\r')
        # Pause execution for 1 second
        time.sleep(1)
        # Increment the second counter
        second += 1

# Define the main function
def main():
    try:
        # Print a welcome message
        print("\nCOUNTDOWN TIMER")  # Welcome message   
        print("-----------------")
        # Wait for the user to press ENTER
        input("Press ENTER To Start The Stopwatch: ")        
        # Call the stopwatch function
        stopwatch()    
    except KeyboardInterrupt:
        # Handle the KeyboardInterrupt exception
        print("\nStopwatch Stopped!\n")

# Check if this script is the main module
if  __name__ == "__main__":
    # Call the main function
    main()  # Call the main function

# Author: GAURAV PANDEY