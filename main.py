import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def speak():
    command = None
    try:
        with sr.Microphone() as source:
            talk("hi i'm listening now")
            talk("what can i do for you")
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'john' in command:
                print(command)
    except:
        pass
    return command


def run_virtual_assistant():
    command = speak()
    if 'play' in command:
        talk("what playlist do you have in mind")
        print("checking youtube...")
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M:%p")
        talk("the current time is "+time)
    elif 'who is' in command:
        person = command.replace('who is','')
        print("searching...")
        info = wikipedia.summary(person,1)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("i didn't get your last command")
while True:
    run_virtual_assistant()