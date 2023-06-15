import speech_recognition as sr
import win32com.client
import webbrowser
from AppOpener import open
import openai
import os
import builtins
import random


def takeCommand():
    r = sr.Recognizer()
    # taking input from mic
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            search = r.recognize_google(audio, language="en-in")
            print(f"User Said: {search}")

            return search
            # Output as voice

        except Exception:
            e = "Some Error Occurred"
            print(e)
            return "clear"


def say(ans):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(ans)


def chat(query):
    global chatStr
    openai.api_key = "your open api key here"

    chatStr = f"User: {query}\n Jarvis: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: wrap this in a try catch
    say(ans=response["choices"][0]["text"])

    chatStr += f"{response['choices'][0]['text']}\n "

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with builtins.open(f"D:\programming\jarvis Ai\Openai\{f'data {random.randint(1, 10000000000)}'}.txt", "w") as f:
        f.write(chatStr)
    print(chatStr)


if __name__ == "__main__":
    while True:

        print("Listening...")

        query = takeCommand()

        if f"Open youtube".lower() in query.lower():
            webbrowser.open("https://www.youtube.com")
            break

        elif f"Open github".lower() in query.lower():
            webbrowser.open("https://www.github.com")
            break

        elif f"Open google".lower() in query.lower():
            webbrowser.open("https://www.google.com")
            break

        elif f"Open wikipedia".lower() in query.lower():
            webbrowser.open("https://www.wikipedia.com")
            break

        elif "Open edge".lower() in query.lower():
            open("Microsoft edge")
            say(ans="opening edge")
            break

        elif "Open brave".lower() in query.lower():
            open("brave")
            say(ans="opening brave")
            break

        elif "Open chrome".lower() in query.lower():
            open("google chrome")
            say(ans="opening google chrome")
            break

        elif "open spotify".lower() in query.lower():
            open("spotify")
            say(ans="opening spotify")
            break
        
        elif "open valorant ".lower() in query.lower():
            open("valorant")
            say(ans="opening valorant")
            break
        
        else:
            chat(query)
