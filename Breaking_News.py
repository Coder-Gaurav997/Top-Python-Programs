# Import required libraries
import requests, pyttsx3 as pts

def get_news():
    try:
        # API key for NewsAPI
        api_key = "31a56db24832499e98eb8f141fd50ac3"
        # Set country to US
        country = "us"
        # Number of headlines to show
        number = 10
        # Construct the API URL
        url = f"http://newsapi.org/v2/top-headlines?country={country}&pageSize={number}&apiKey={api_key}"

        # Send GET request to the API
        response = requests.get(url)
        # Parse JSON response
        data = response.json()
        if not data:  # Check if data is empty
            print("Sorry! No News Available Now")
        
        return data
    except Exception as e:
        print("\nOpps! There Is No Internet Connection.")

def speak(text):
    # Initialize text-to-speech engine
    engine = pts.init()
    # Convert text to speech
    engine.say(text)
    # Play the speech
    engine.runAndWait()

# Fetch news data
news = get_news()

def main():
    try:
        print("\n-- BREAKING NEWS OF USA --\n")

        # Loop through each headline in the news articles
        for i, headline in enumerate(news["articles"]):
            # Print the headline with a number
            print(f"{i+1}) {headline['title']}")
            # Read the headline aloud
            speak(headline["title"])
        print("")
    except Exception as e:
        print("",end="")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()

# Author: GAURAV PANDEY    