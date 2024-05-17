import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine  = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")

    speak("hello ronit sir I am jarvis  please tell me that how may i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...")    
        return "None" 
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('singharonit22@gmail.com', 'SINGHA@ronit@011002')
    server.sendmail('singharonit22@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    WishMe()
    while True:
     #if 1:
        query = takeCommand().lower()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        
        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("in Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open makaut' in query:
            webbrowser.open("https://makautexam.net/")

        elif 'open irctc' in query:
            webbrowser.open("irctc.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open my college' in query:
            webbrowser.open("https://bcrec.ac.in/")

        elif 'open map' in query:
            webbrowser.open("https://www.google.com/maps/@23.3491036,85.3446311,15z?entry=ttu")

        elif 'open chat gpt' in query:
            webbrowser.open("https://chat.openai.com/")


        elif 'play music' in query:
            music_dir = 'D:\\my songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ronit Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open steam ' in query:
            steamPath = "D:\\steam\\Steam.exe"
            os.startfile(steamPath)


        elif 'email to ronit' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "singharonit17@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry ronit sir. i am not able to send this email")

