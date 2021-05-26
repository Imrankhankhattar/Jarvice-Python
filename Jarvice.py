
import datetime
import pyttsx3
import speech_recognition as SR
import wikipedia
import webbrowser
import os
import smtplib
import time
import pywhatkit
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis here Mister IMRAN. Please tell me how may I help you ")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('imkhattar999@gmail.com', 'imran khan 41')
    server.sendmail('imkhattar999@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    # wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'close chrome' in query:
            os.system("taskkill /im chrome.exe /f")

        elif 'open stackoverflow' in query or 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:  # take it with random
            music_dir = 'C:\\Users\\imran khan\\Music\\SONGS'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code blocks' in query:
            codePath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codePath)
            print("openning Code Blocks...Please wait for 30 seconds")
            time. sleep(40)
        elif 'open vscode' in query or 'open vs code' in query:
            codePath = 'C:\\Users\\imran khan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
            print("openning VS CODE...Please wait for 30 seconds")
            time. sleep(40)
        elif 'email to imran' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ik3484770@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend IMRAN. I am not able to send this email")

        elif 'thanks' in query or 'great job' in query or 'thank you' in query:
            speak("Pleasure is mine")
        elif 'are you single' in query:
            speak('I am in a relationship with wifi')
        elif 'joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif 'stop for a while' in query or 'wait' in query or 'please wait' in query:
            try:
                timelist = [" seconds", " minutes", "left"]
                speak("How much time???")
                query = takeCommand()

                # extracting digits from string in tuple
                Wait_time = [int(i) for i in query.split() if i.isdigit()]

                if "seconds" in query or "seconds " in query:
                    print("OK waiting for you...!")
                    while Wait_time[0] >= 1:
                        print(str(Wait_time[0])+timelist[0]+" "+timelist[2])
                        Wait_time[0] = Wait_time[0]-1
                        time.sleep(1)
                elif "minute" in query or "minutes" in query:
                    print("OK waiting for you...!")
                    while Wait_time[0] >= 1:
                        i = 60
                        while i >= 1:
                            if Wait_time[0] > 1:
                                print(
                                    str(Wait_time[0]-1)+timelist[1]+" "+str(i)+timelist[0] + " "+timelist[2])
                            else:
                                print(" "+str(i)+timelist[0] + " "+timelist[2])
                            time.sleep(1)
                            i = i-1
                        Wait_time[0] = Wait_time[0]-1
            except Exception as e:
                print(e)

        elif 'exit' in query or 'quit' in query:
            break
            exit()
