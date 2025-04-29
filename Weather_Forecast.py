from geopy.geocoders import Nominatim
import requests

def get_coordinates():
    try:
        print("\nTODAY'S WEATHER FORECASTS")
        print("-------------------------")

        city_name = input("Enter The Name Of City: ")

        # Initialize geolocator with a user agent
        geolocator = Nominatim(user_agent="Gaurav")
        # Get location information for the entered city
        location = geolocator.geocode(city_name)

        return location.latitude, location.longitude, city_name
    except Exception as e:
        print(f"Sorry! An Error Occured: {e}\n")
        
def get_weather():
    try:  
        api_key = "YOUR_OPENWEATHER_API"
        # Construct URL for OpenWeatherMap API request
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

        # Send GET request to the API
        response = requests.get(url)
        # Parse JSON response
        weather = response.json()

        return weather
    except Exception as e:
        print(f"Sorry! An Error Occured: {e}\n")

# Get coordinates and city name from user input
latitude, longitude, city_name = get_coordinates() 
# Fetch weather data using the coordinates
weather = get_weather()

def main():
    try:
        print(f"\nWEATHER DETAILS OF {city_name.upper()}:\n")
        print(f"Latitudes: {latitude}")
        print(f"Longitudes: {longitude}\n")

        # Display weather information
        print(f"Temperature: {weather['main']['temp']-273:.2f} C")    # Convert Kelvin to Celsius
        print(f"Humidity: {weather['main']['humidity']} %")
        print(f"Wind Speed: {weather['wind']['speed']*18/5:.2f} km/h")  # Convert m/s to km/h
        print(f"Pressure: {weather['main']['pressure']*0.0145:.2f} psi")  # Convert hPa to psi
        print(f"Description: {weather['weather'][0]['description'].upper()}\n")
    except Exception as e:
        print("Oops! Unable To Fetch Weather.\n")

if  __name__ == "__main__":
    main()

# Author: GAURAV PANDEY
