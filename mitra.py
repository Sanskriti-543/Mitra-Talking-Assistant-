import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning master!")
        talk("Good Morning master!")


    elif hour>=12 and hour<18:
        print("Good Afternoon master!")   
        talk("Good Afternoon master!") 

    else:
        talk("Good Evening master!") 


    print("I am your assistant.  How may I help you?")   
    talk("I am your assistant.  How may I help you?")




def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
    except:
        pass
    return command


if __name__ == "__main__":
    wishMe()

def run_alexa():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        print(song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is ' + time)

    elif 'what is ' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    if 'wikipedia' in command:
            talk('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            talk("According to Wikipedia")
            print(results)
            talk(results)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'open youtube' in command:
            webbrowser.open("youtube.com")

    elif 'open google' in command:
            webbrowser.open("google.com")

    elif 'open stackoverflow' in command:
            webbrowser.open("stackoverflow.com") 

    else:
        talk('Please say the command again.')


while True:
    run_alexa()