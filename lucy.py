# import required libraries
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import urllib.request
import urllib.parse
import re
import pyautogui
import psutil
import pyjokes

#Initialise text to speech
engine=pyttsx3.init()

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Fuction to get current time
def time():
    Time= datetime.datetime.now().strftime("%I:%M:%S")
    speak("The time is")
    speak(Time)

# Function to get current date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("today's date is") 
    speak(date)
    speak(month)
    speak(year)

# Greeting function for greeting according to the time(morning/afternoon/evening/night)
def wishme():
    speak("Hello! Welcome back mam!")    
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning mam!")
    elif hour>=12 and hour<18:
        speak("Good afternoon mam!")
    elif hour>=18 and hour<24:
        speak("Good Evening mam!")
    else:
        speak("Good night mam!")
    
    speak("Lucy at your service mam! how can I help you? I can do following tasks for you:")
    print("1. Date 2. Time 3. Wikipedia 4. Chrome search anything 5. Logout_Shut down_restart system 6. Play vedio on You Tube 7. Take notes 8. Ask for stored notes 9. Take screenshot 10. CPU status 11. Ask for some funny jokes 12. Logout")
    speak("1.Date 2.Time 3.Wikipedia 4.Chrome search anything 5.Logout_Shut down_restart system 6.Play vedio on You Tube 7.Take notes 8.Ask for stored notes 9.Take screenshot 10.CPU status 11.Ask for some funny jokes 12.Logout")

# Function to take commands from user
def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    
    except Exception as e:
        print(e)
        speak("Sorry mam i could not understand...")
        return "None"
    return query

# Function to take screenshot
def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/Srishiti/Desktop/ss.png")

# Function to tell battery usage and percentage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

# Function to tell jokes
def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:                                 
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:                               #reads the summary from the wikipedia search
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'search in chrome' in query:                        #search and open the chrome page for the given keyword
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        
        elif 'logout' in query:                   
            os.system("shutdown -l")                              
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play on youtube' in query:                       #play the first recommended you tube video for the serach
            speak("what do you want me to play?")
            query_s = takeCommand().lower()
            words = query_s.split()
            url = "http://www.youtube.com/results?search_query="
            for word in words:
                  url = url + word + "+"  
            wb.open_new(url)
        
        elif 'note' in query:                                #remember the notes from user
            speak("What should I note?")
            print("What should I note?")
            data = takeCommand()
            speak("you said me to note that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'What did I ask you to note?' in query:         #tell user about the stored notes
            remember =open('data.txt', 'r')
            speak('you said me to remember that' +remember.read())
        
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        
        elif 'cpu' in query:
            cpu()
        
        elif 'joke' in query:
            jokes()
            while True:
                speak('Do you want to listen more?')
                choice = input("yes/no: ")
                if choice=='yes':
                    jokes()
                elif choice == 'no':
                    break

        elif 'offline' in query:
            quit()

