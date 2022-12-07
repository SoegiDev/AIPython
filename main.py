from ast import Not
from jarvis import JarvisAssistant
import re
import os
import random
import pprint
import datetime
import requests
import sys
import urllib.parse  
import pyjokes
import time
import pyautogui
import pywhatkit
from PIL import Image

obj = JarvisAssistant()

TANYA_JAM = ["what time is it", "time is it", "time now", "jam berapa sekarang"]


GREETINGS = ["hello jarvis", "jarvis", "you there jarvis", "hey jarvis",
             "ok jarvis","okey jarvis","okay jarvis", "are you there", "hello michelle", "hello","michele"]

GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

THANK = ["thank you"]
THANKS_RES = ["welcome sir","Don't mention it Sir","No Problem Sir","Anytime Sir","It's my pleasure Sir","No worries Sir"]

WAKUP_FROM_SLEEP=['wake up jarvis']
WAKUP_FROM_SLEEP_RES=["I'm awake Sir","I'm ready Sir","I've seen the world Sir"]

EXCEPT = ["Please try again"]
CANNOT_HEAR = ["I can not hear sir","do you have any other questions, sir","next question sir","not clear sound, sir"]


def speak(text):
    obj.tts(text)

def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")
# if __name__ == "__main__":
if __name__ == "__main__":
        wish()
        time = 0
        while True:
            command = obj.mic_input()
            if time>3 :
                time =0
                speak(random.choice(CANNOT_HEAR))
            
            if re.search('what time is it', command):
                date = obj.tell_time()
                print(date)
                speak(f'{date} Sir')

            if re.search('what date is it today', command):
                date = obj.tell_me_date()
                print(date)
                speak(f'{date} Sir')

            if command in GREETINGS:
                speak(random.choice(GREETINGS_RES))

            if command in WAKUP_FROM_SLEEP:
                speak(random.choice(WAKUP_FROM_SLEEP_RES))
            
            if command in THANK:
                speak(random.choice(THANKS_RES))

            if re.search('open', command):
                    domain = command.split(' ')[-1]
                    open_result = obj.website_opener(domain)
                    speak(f'Alright sir !! Opening {domain}')
                    print(open_result)
            if 'search google for' in command:
                    obj.search_anything_google(command)
                    
            if 'playing on youtube' in command:
                    video = command.split(' ')[3]
                    speak(f"Okay sir, playing {video} on youtube")
                    pywhatkit.playonyt(video)
                    
            if "where i am" in command or "current location" in command or "where am i" in command:
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak("Sorry sir, I coundn't fetch your current location. Please try again")
            
            if "goodbye jarvis" in command or "go home" in command:
                    value = command.split(' ')[2]
                    #speak(f"Okay sir, Go Home")
                    valueset = obj.run_alarm(value)
                    # speak(f"Okay sir, Thank you Sir. I'am Go to Sleep")
                    speak(f"Okay sir, Done. Set Go Home")

            if "ip address" in command:
                    ip = requests.get('https://api.ipify.org').text
                    print(ip)
                    speak(f"Your ip address is {ip}")

            if "take screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                    speak("By what name do you want to save the screenshot?")
                    name = obj.mic_input()
                    speak(f"Alright sir, taking the screenshot with the name {name}")
                    img = pyautogui.screenshot()
                    name = f"{name}.png"
                    img.save(name)
                    speak("The screenshot has been succesfully captured")

            if "show me the picture" in command:
                    try:
                        speak("what is the name of the picture")
                        name = obj.mic_input()
                        img = Image.open('E://GITLAB//PUBLIC//PYTHON//ai-jarvis//' + name+".png")
                        img.show(img)
                        speak("Here it is sir")
                    except IOError:
                        speak("Sorry sir, I am unable to display the screenshot")
            
            if re.search('tell me about', command):
                    topic = command.split(' ')[-1]
                    if topic:
                        wiki_res = obj.tell_me(topic)
                        print(wiki_res)
                        speak(wiki_res)
                    else:
                        speak(
                            "Sorry sir. I couldn't load your query from my database. Please try again")
            
            if re.search('weather', command):
                    city = command.split(' ')[-1]
                    weather_res = obj.weather(city=city)
                    print(weather_res)
                    speak(weather_res)

            if "buzzing" in command or "news" in command or "headlines" in command:
                    news_res = obj.news()
                    speak('Source: The Times Of Indonesia')
                    speak('Todays Headlines are..')
                    for index, articles in enumerate(news_res):
                        pprint.pprint(articles['title'])
                        speak(articles['title'])
                        if index == len(news_res)-2:
                            break
                    speak('These were the top headlines, Have a nice day Sir!!..')

            if "system" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)

            else :
                time +=1