import urllib
import speech_recognition as sr
import sys
import wave
import pyttsx3
import os
import webbrowser
import datetime
from bs4 import BeautifulSoup
import requests
import sounddevice as sd
from time import ctime
from scipy.io.wavfile import write
now=datetime.datetime.now()
r=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
print("How may i help you")
engine.say("How may i help you?")
engine.runAndWait()
def record_audio():
    with sr.Microphone() as source:
        print("Listening!!")
        audio=r.listen(source)
    try:
        data=r.recognize_google(audio)
        print(data)
    except sr.UnknownValueError:
        print("Sorry,I did not get that")
    except sr.RequestError:
        print('Sorry, my speech service is down')
    except sr.UnboundLocalError:
        print('Sorry,I did not get that')
    return data
while 1:
    
    a=record_audio()
    if(a=="hi"):
        engine.say("hi")
        engine.runAndWait()
        print("Hi")
    elif(a=="open the browser"):
        engine.say("Opening Browser")
        engine.runAndWait()
        webbrowser.open('https://www.bing.com')
    elif(a=="display time"):
        engine.say("the time is")
        engine.runAndWait()
        h=now.hour
        m=now.minute
        print("Current hour: %d" % now.hour)
        print("Current min: %d" % now.minute)
        engine.say(h)
        engine.say(m)
        engine.say("minutes")
    elif(a=="open Excel"):
        engine.say("opening excel")
        engine.runAndWait()
        os.system("start excel.exe")
    elif(a=="exit"):
        exit()
    elif(a=="open Notepad"):
        engine.say("opening notepad")
        engine.runAndWait()
        os.system("start notepad.exe")
    elif(a=="open calculator"):
        engine.say("opening calculator")
        engine.runAndWait()
        os.system("start calc.exe")
    elif(a=="open a file"):
        print("Mention the type of file")
        engine.say("Mention type of file")
        engine.runAndWait()
        b=input()
        if(b=="docx"):
            print("Enter filename")
            engine.say("Enter filename")
            engine.runAndWait()
            c=input()
            engine.say("Opening now")
            engine.runAndWait()
            os.system(c+".docx")
        elif(b=="text"):
            print("Enter a filename")
            engine.say("Enter a filename")
            engine.runAndWait()
            c=input()
            engine.say("Opening now")
            engine.runAndWait()
            os.system(c+".txt")
        elif(b=="image"):
            print("Enter a Filename")
            engine.say("Enter a Filename")
            engine.runAndWait()
            c=input()
            engine.say("Opening now")
            engine.runAndWait()
            os.system(c+".jpg") 
    elif(a=="get html of website"):
        print("Enter URL")
        engine.say("Enter URL")
        engine.runAndWait()
        c=input()
        page=requests.get(c)
        soup=BeautifulSoup(page.content,'html.parser')
        print(soup.prettify())
    elif(a=="create a text file"):
        h=input("Enter a name")
        engine.say("Enter A name")
        engine.runAndWait()
        file=open(h+'.txt','x')
        b=input("What do you wanna write?")
        engine.say("What do you wanna write?")
        engine.runAndWait()
        file.write(b)
        file.close()
    elif(a=="record"):
        print("Recording started:")
        engine.say("Recording started")
        engine.runAndWait()
        fs=44100
        second=10
        myrecording=sd.rec(int(second*fs),samplerate=fs,channels=2)
        sd.wait()
        write('speech13.wav',fs,myrecording)
    elif(a=="ok google"):
        new=2
        taburl="http://google.com/search?q=";
        with sr.Microphone() as source:
            print("What do you want to search for?")
            engine.say("What do you want to search for?")
            engine.runAndWait()
            g=r.listen(source)
        
        term=r.recognize_google(g)
        webbrowser.open(taburl+term,new=new);
    elif(a=="open firefox"):
        engine.say("Opening firefox");
        engine.runAndWait();
        os.system("start firefox.exe");
    elif(a=="tell me about yourself"):
        engine.say("Iam a software written in python");
        engine.runAndWait();
        engine.say("I am still at development stage");
        engine.runAndWait();
    
    elif(a=="exit"):
        sys.exit()
    elif(a=="map"):
        print("inside elif")
        val=2
        url="http://google.co.in/maps/place/";
        with sr.Microphone() as source:
            print("name the location")
            engine.say("name the location")
            engine.runAndWait()
            loca=r.listen(source)
        try:
            location=r.recognize_google(loca)
        except sr.UnknownValueError:
            print("Sorry,I did not get that")
        except sr.RequestError:
            print('Sorry, my speech service is down')
        except sr.UnboundLocalError:
            print("\n ")
        webbrowser.get().open(url+location,new=val);
    elif(a=="what is your name" or "whats your name"):
        print("My name is lino")
        engine.say("My name is Lino")
        engine.runAndWait();
    elif(a=="whats the time now" or "what time is it" or "today's date" or "current time" or "what day is it"):
        print(ctime())

        
        
        
    


        

    
    
    
