import os
import webbrowser
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

engine.setProperty("rate", 170)


def speak(text):
    print("AI :", text)
    engine.say(text)
    engine.runAndWait()


def take_command():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=5
        )

    try:

        command = recognizer.recognize_google(audio)

        command = command.lower()

        print("You :", command)

        return command

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")

    except sr.RequestError:
        speak("Internet connection required.")

    except Exception:
        speak("Something went wrong.")

    return ""


def run_assistant():

    speak("Hello Aarya. How can I help you?")

    command = take_command()

    if not command:
        return

    if "google" in command:

        webbrowser.open("https://www.google.com")

        speak("Opening Google")

    elif "youtube" in command:

        webbrowser.open("https://www.youtube.com")

        speak("Opening YouTube")

    elif "calculator" in command:

        os.system("calc")

        speak("Opening Calculator")

    elif "notepad" in command:

        os.system("notepad")

        speak("Opening Notepad")

    elif "chrome" in command:

        os.system("start chrome")

        speak("Opening Chrome")

    elif "chat g p t" in command or "chatgpt" in command:

        webbrowser.open("https://chat.openai.com")

        speak("Opening ChatGPT")

    elif "shutdown" in command:

        speak("Shutdown command is disabled for safety.")

    elif "exit" in command or "stop" in command:

        speak("Goodbye Aarya.")

    else:

        speak("Sorry, I don't know that command yet.")