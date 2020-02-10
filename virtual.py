import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random


engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your virtual Assistant George , how may i help you ? ")

def takeCommand():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing......")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said :{query}\n")

    except Exception as e:
        print("say it again please...")
        speak("say that again please..")

        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com","password")
    server.sendmail("abc@gmail.com",to,content)
    server.quit()




if __name__ == "__main__" :
    wishMe()
    while True:

        query=takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif "play music" in query:
            music_dir=(r"C:\Users\My\Music")
            songs=os.listdir(music_dir)
            sng=random.randint(0,109)
            os.startfile(os.path.join(music_dir,songs[sng]))
            quit()

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif "the date" in query:
            strDate = datetime.datetime.now().strftime("%y-%m-%d")
            speak(f"sir, the date is {strDate}")

        elif "open code" in query:
            codepath=(r"C:\Users\My\PycharmProject\virtualAss.py\VA.py")
            os.startfile(codepath)

        elif "mail to bond" in query:
            try:
                speak("What should i say?")
                content=takeCommand()
                to="abc@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                speak("Email has not been send")

        elif "calculator" in query:
             codepath=(r"C:\Users\My\PycharmProject\tkinter1\calculator.py")
             os.startfile(codepath)

        elif "play game" in query:
            os.startfile(r"C:\Users\My\PycharmProject\tkinter1\dist\tic_tac_toe.exe")

        elif "how are you" in query:
            speak("i am fine sir what about you")

        elif "what's your name" in query:
            speak("i am your assistant ,George")

        elif "hello"  in query:
            speak("hello sir, how are you")

        elif "how old are you" in query:
            speak("i am 18 year old")

        elif "what are you doing" in query:
            speak("Nothing sir, just trying to help you")

        elif "stop" in query or "exit" in query:
            quit()
