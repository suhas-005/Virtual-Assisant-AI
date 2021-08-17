import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes

engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    elif hour>18 and hour<=20:
        speak("Good Evening")
    else:
        speak("Hello")
    speak("I am Kiara, How may I help you.")   


def recognize():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"Recognized:{query}\n")

    except Exception as e:
        speak("Sorry I did not get you...")
        return "none"
    return query

if __name__ == "__main__":
    greet() 
    while True:
        query = recognize().lower()
        if "time" in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak(time)

        elif "date" in query:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            date = datetime.datetime.now().day
            speak(f"Today's date is {date} {month} {year}")
            
        elif "chrome" in query:
            loc = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(loc)

        elif "movie" in query:
            movie_dir = r"**GIVE PATH TO MOVIES FOLDER HERE**"
            movie = os.listdir(movie_dir)
            rd = random.choice(movie)
            os.startfile(os.path.join(movie_dir, rd))
        
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Adress is {ip}")
        
        elif "wikipedia" in query:
            speak("Looking into Wikipedia...")
            query = query.replace("wikipedia", "")
            res = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(res)
            print(res)
        
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "open netflix" in query:
            webbrowser.open("www.netflix.com")
        
        elif "open amazon" in query:
            webbrowser.open("www.amazon.in")

        #elif "whatsapp" in query:
            #kit.sendwhatmsg("NUMBER", "TEXT",2,25)

        elif "play music" in query:
            speak("Which song do you like listen")
            cm = recognize().lower()
            kit.playonyt(f"{cm}")

        elif "search on google" in query:
            speak("What may I help you to find")
            lis = recognize().lower()
            kit.search(f"{lis}")

        elif "favourite song" in query:
            kit.playonyt("https://www.youtube.com/watch?v=PJWemSzExXs")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "take note" in query:
            speak("What should I write down")
            memory = recognize().lower()
            speak("Noted")
            note = open("note.txt", "w")
            note.write(memory)
            note.close()

        elif "remind me" in query:
            note = open("note.txt", "r")
            speak("You asked me to remember that" +note.read())        

        elif "no thanks" in query:
            speak("Have a Nice Day")
            sys.exit()

        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        speak("May I help you with anything else")
