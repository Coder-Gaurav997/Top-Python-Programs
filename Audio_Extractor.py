""" Audio Extractor """

# Import the necessary libraries
import tkinter as tk
from tkinter.filedialog import *  # Import file dialog for GUI
from moviepy.editor import VideoFileClip  # Import VideoFileClip for video processing

# Function to extract audio from a video file
def audio_extractor():
    try:
        # Create a Tkinter root window (required for file dialog)
        root = tk.Tk()
        # Open a file dialog to select a video file
        video = VideoFileClip(askopenfilename())
        # Close the Tkinter root window
        root.destroy()
        # Print video selected succussful message
        print("Video File Selected Successfully!")
        # Prompt the user to enter a name for the audio file
        name = input("Enter The Name For The Audio File [Default: Audio.mp3]: ")
        # If no name is provided, use the default name
        if not name:
            name = "Audio.mp3"
            # Write the audio to a file with the default name
            video.audio.write_audiofile(name)
        else:
            # Write the audio to a file with the provided name and .mp3 extension
            video.audio.write_audiofile(name + '.mp3')
        # Close the video file
        video.close()
    except Exception:
        # Handle any exceptions that occur during audio extraction
        print("UNABLE TO EXTRACT AUDIO!\n")

# Main function to run the audio extractor
def main():
    # Print a header for the audio extractor
    print("\nAUDIO EXTRACTOR")
    print("---------------")
    # Call the audio extractor function
    audio_extractor()

# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function
    main()

# Author: GAURAV PANDEY