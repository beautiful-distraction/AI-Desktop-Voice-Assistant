import pyttsx3 #modules used in this program
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import pywhatkit as wk 
import sys
import pyautogui
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    speak("welcome back bro")
    print("welcome back bro")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning Baabaii!")
    elif hour>=12 and hour<18:
        speak("good afternoon baavee!")
    else: 
        speak("good Evening baavee!")

    speak("i am chachu ,bro how may i help you")
def takeCommand():
    #it will take micrphone input from the user and returns string
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("boool brooo i am listening...")
        speak("boool brooo i am listening...")
        r.pause_threshold = 1
        r.energy_threshold = 0.8 
        audio = r.listen(source,timeout=10,phrase_time_limit=5)


    try:
    
        print("ruuk... bro i am working on it...")
        speak("ruuk....bro i am working on it...")
        query =r.recognize_google(audio,language='en-in')
        print (f"User said:{query}\n")

    except Exception as e:
        #print(e)
        print("bro...say that again ")
        speak("bro...say that again ")
        return "None"
    return query
    // you have to fill your personal data
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',//generated number)
    server.ehlo()
    server.starttls()
    server.login('gmail', 'temp generated password')
    server.sendmail('gmail', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
    
    # code for exicuting given task
      
        if 'wikipedia' in query:
            speak('Searching Wikipedia baaaveee...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("brooo..According to Wikipedia")
            print(results)
            speak(results)

        elif 'just open youtube' in query:
            webbrowser.open("youtube.com")
        elif'open youtube' in query:
            speak("bro.. what you will like to watch?")
            query = takeCommand().lower()
            wk.playonyt(f"{query}")
        elif 'search on youtube' in query:
            query = query.replace("search on youtube","")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")



        elif 'just open google' in query:
            webbrowser.open("google.com")
        elif 'open google' in query:
            speak("what should I search? bro")
            query = takeCommand().lower()
            webbrowser.open(f"{query}")
            results = wikipedia.summary(query,sentences=1)
            speak(results)


        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'close browser'in query:
            os.system("taskkill /f /im msedge.exe")


        elif 'the time' in query: 
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"baavee,time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Karan Bansha\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)
        elif 'open MS word' in query:
            codePath="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)
        elif 'joke' in query:
            speak(pyjokes.get_jokes())
        elif 'email to nikhil' in query:
            try:

                speak("bro..what should i say?")
                content = takeCommand()
                to = "bhardwajnikhil019@gmail.com"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry bro....Iam not able to send this email")


        elif 'email to Arun' in query:
            try:
                 speak("bro..what should i say?")
                 content = takeCommand()
                 to = "koundalarun93@gmail.com"
                 sendEmail(to,content)
                 speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry bro....Iam not able to send this email")


        elif 'email to nikshita' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "nikshita2002@gmail.com"
                sendEmail(to,content)
                speak("email has been send!")
            except Exception as e:
                print(e)
                speak("sorry bro...Iam not able to send this email")


        elif 'email to Sanjeev sir' in query:
            try:
                speak("bro..what should i say?")
                content = takeCommand()
                to = "sanjeevkhan.hpu@gmail.com"
                sendEmail(to,content)
                speak("email has been send!")
            except Exception as e:
                prin(e)
                speak("sorry bro...Iam not able to send this email")

        elif 'open hpu data science and ai site' in query:
            webbrowser.open("https://hpuniv.ac.in/university-detail/home.php?science-and-artificial-intelligence")
        
#for restart and sleep and shutdown computer
        elif'sleep mode' in query:
            os.system("rundll32.exe powerprof.dll,setsuspendstate 0,1,0")
        elif"shutdown the system" in query:
            os.system("shutdown/s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /e /t 5")
        
            
