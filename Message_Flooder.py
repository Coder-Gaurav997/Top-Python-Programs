import pyautogui as pyag  # For simulating keyboard input
import pyttsx3 as pts     # For text-to-speech functionality
import winsound           # For playing sound alerts
import time               # For adding delays

# Initialize the text-to-speech engine
engine = pts.init()

def flooder(message, times):
    """
    Simulates typing a message multiple times in the active window.
    
    Args:
        message (str): The message to be typed.
        times (int): The number of times the message should be typed.
    """
    message = message.split(" ")  # Split the message into words
    for _ in range(times):        # Repeat the process 'times' number of times
        for word in message:      # Iterate through each word in the message
            for letter in word:   # Iterate through each letter in the word
                pyag.press(letter)  # Simulate pressing the letter key
            pyag.press('space')     # Simulate pressing the spacebar after each word
        pyag.press('enter')         # Simulate pressing the enter key after each message

def main():
    """
    Main function to execute the message flooding process.
    """
    print("\nMESSAGE FLOODER")
    print("---------------")
    
    # Get user input for the message and the number of times to flood
    message = input("Enter The Message To Flood: ")
    times = int(input("Enter Number Of Times To Flood: "))
    
    # Countdown using text-to-speech
    engine.say("3")
    engine.runAndWait()
    time.sleep(0.5)
    engine.say("2")
    engine.runAndWait()
    time.sleep(0.5)
    engine.say("1")
    engine.runAndWait()
    time.sleep(0.5)    

    # Play a beep sound to signal the start of flooding
    winsound.Beep(2000, 700)
    
    # Call the flooder function to start the flooding process
    flooder(message, times)
    # Print successful message
    print(f"\n-- Message '{message}' Has Been Flooded {times} Times Successfully --\n")

# Entry point of the script
if __name__ == "__main__":
    main()

# Author: GAURAV PANDEY