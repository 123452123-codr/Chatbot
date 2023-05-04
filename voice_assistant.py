import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("Hello, I am your guide to Sustainable Development Goals. I am here to help you with the SDG goals.")


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ask me anything about them...")
        speak("Ask me anything about them...")
        r.pause_threshold = 3
        audio = r.listen(source)

    try:
        print("Recognizing...")
        q = r.recognize_google(audio, language="en-in")
        query_list = [q]
        for i in query_list:
            print(i)

    except Exception as e:
        print(e)

        print("Say that again..")
        return "None"
    return q


if __name__ == '__main__':
    wish()
    while True:
        q = command().lower()

        if 'wikipedia' in q:
            speak("Searching Wikipedia...")
            q = q.replace("Wikipedia", "")
            results = wikipedia.summary(q, sentences=2)
            speak("According to Wikipedia,")
            print(results)
            speak(results)

        elif 'thank you' in q:
            break


