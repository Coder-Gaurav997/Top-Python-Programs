# Import the gTTS (Google Text-to-Speech) module
from gtts import gTTS

# Welcome message
print("\nGOOGLE TEXT-TO-SPEECH")
print("---------------------")

# Prompt the user to enter the text they want to convert to speech
text = input("\nEnter The Text To Convert Into Speech: ")

# Prompt the user to enter a name for the output MP3 file
name = input("Enter The Name For 'MP3' File [Default: Output.mp3]: ")

try:
    # Create a gTTS object with the user's text and specify English as the language
    speak = gTTS(text=text, lang='en')

    # Check if the user provided a name for the file
    if not name:
        # If no name was provided, use a default name "Output.mp3"
        name = "Output.mp3"
        # Save the speech as an MP3 file with the default name
        speak.save(name)
    else:
        # If a name was provided, add ".mp3" extension to it and save the file
        speak.save(name + ".mp3")
    print("\nFILE SAVED SUCCESSFULLY\n")  # Print succeess message

except Exception as e:
    print(f"An error occured: {e}\n")

# Author: GAURAV PANDEY