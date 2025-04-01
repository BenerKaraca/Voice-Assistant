import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import subprocess

recognizer = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
            return query.lower()
        except Exception as e:
            print("Sorry, I didn't catch that. Could you please repeat?")
            return None

def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {current_time}")

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    speak(f"Here are the search results for {query}")

def open_application(app_name):
    try:
        if os.name == 'nt':  # For Windows
            os.startfile(app_name)
        elif os.name == 'posix':  # For macOS and Linux
            subprocess.call(["open", "-a", app_name])
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"Sorry, I couldn't open {app_name}")

def open_game():
    game_path = r"C:Fortnite.url"  # Adjust the path to your game
    try:
        os.startfile(game_path)  # Open the Fortnite URL file
        speak("Opening Fortnite!")
    except Exception as e:
        speak(f"Sorry, I couldn't open the game. Error: {e}")

def main():
    speak("Before we start, may I know your name?")
    name = listen()
    speak(f"Hello {name}!, I'm your voice assistant HUE. How can I help you?")

    while True:
        query = listen()
        if query:
            if "time" in query:
                tell_time()
            elif "search" in query:
                search_query = query.replace("search", "").strip()
                search_web(search_query)
            elif "open" in query:
                app = query.replace("open", "").strip()
                open_application(app)
            elif "best game" in query:  # When user says 'game'
                open_game()  # Open the Fortnite game
            elif "exit" in query or "bye" in query:
                speak("Goodbye! Have a great day!")
                break
            else:
                speak("I'm sorry, I don't understand that command. Can you please try again?")

if __name__ == "__main__":
    main()
