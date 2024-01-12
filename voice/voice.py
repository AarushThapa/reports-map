import pyttsx3
import speech_recognition as sr
import datetime

listener = sr.Recognizer()


engine = pyttsx3.init()
voices = engine.getProperty('voices')  
engine.setProperty('voice', voices[123].id) 


# for idx, voice in enumerate(voices):
#     print(f"Voice {idx} - ID: {voice.id}, Name: {voice.name}, Lang: {voice.languages}")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        speak("Try speaking now")
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            command_list(command)
    except:
        speak("Invalid Command")


def command_list(command):
    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time}")
    if "date" in command:
        date = datetime.datetime.today().date()
        speak(f"Today is {date}")

if __name__ == "__main__":
    speak("Lets Speak")
    while True:
        listen()