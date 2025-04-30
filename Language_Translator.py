# Importing Modules
from deep_translator import GoogleTranslator

# Translator Function
def translate_text(text, target_language="hi"):
    translated_text = GoogleTranslator(source="auto", target=target_language).translate(text)
    return translated_text

# Dictionary of the language codes
dict = {'English' : 'en',
        'Hindi' : 'hi',
        'Tamil' : 'ta',
        'Marathi' : 'mr',
        'Urdu' : 'ur',    
        'Punjabi' : 'pa',
        'Bengali' : 'bn',
        'Telugu' : 'te',
        'Malayalam' : 'ml',
        'Kannada' : 'kn',
        'German' : 'de'}

# Print welcome message
print("\nWELCOME TO TRANSLATOR")
print("---------------------")

# Ask to show the language codes dictionary
try:
    choice = input("\nDo you want to see the dictionary of language codes [Y/N]: ").lower()
    if choice == 'y':
        print(f"Languages Codes: {dict}")
    else:
        pass

    # Translating The Given Text
    if __name__ == "__main__":
        user_text = input("\nEnter the text to translate: ")
        target_language = input("Enter the target language code (e.g: 'hi' for Hindi): ")

    # Show The Translated Text
        translated_result = translate_text(user_text, target_language)
        print(f"\nTranslated text: {translated_result}")
except Exception as e:
    print("\nOpps! No Internet Connection\n")

# Author: GAURAV PANDEY