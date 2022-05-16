from http import server
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that again please...")
        return "none"
    return query

def wish():
    hour = (datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis. please tell me how can help you")

#to send mail 
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email','your password')
    server.sendmail('your email', to, content)
    server.close()

if __name__ == "__main__":
    wish()
    # while True:
    if 1:
        query = takecommand().lower()

        if "open notepad" in query:
            path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)

        elif "open command" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            anws = wikipedia.summary(query, sentences=4)
            speak("according to wikipedia")
            speak(anws)
            print(anws)
        
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send message" in query:
            pywhatkit.sendwhatmsg("+91", "this is my python project",19,12)

        elif "play songs" in query:
            speak("sir,what you want to listen")
            cm1 = takecommand().lower()
            pywhatkit.playonyt(f"{cm1}")

        elif "send email" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "receiver email"
                sendEmail(to,content)
                speak("email has been sent successfully")

            except Exception as e:
                print(e)
                speak("sending fail")

        elif "no thanks" in query:
            speak("thanks for using sir,have a good day")
            sys.exit()
        
        speak("sir, do you have any other work" )



        

        
    # takecommand()
    # speak("this is advance jarvis")
