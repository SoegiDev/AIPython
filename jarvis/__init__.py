import speech_recognition as sr
import pyttsx3

from jarvis.features import date_time
from jarvis.features import website_open
from jarvis.features import google_search
from jarvis.features import loc
from jarvis.features import alarm_wakeup
from jarvis.features import wikipedia
from jarvis.features import weather
from jarvis.features import news
from jarvis.features import systems_stats
from time import sleep
import winsound
from jarvis.features import time_go
import winsound
import threading
import random
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[0].id)
engine.setProperty('voice', 'id')
Cannot_hear_RES = ["I can not hear, sir","do you have any other questions, sir","next question, sir","not clear sound, sir"]

class JarvisAssistant:
    def __init__(self):
        pass

    def mic_input(self):
        """
        Fetch input from mic
        return: user's voice input as text if true, false if fail
        """
        try:
            r = sr.Recognizer()
            # r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source, duration=1)
            with sr.Microphone() as source:
                print("Listening....")
                r.energy_threshold = 4000
                audio = r.listen(source,phrase_time_limit = 5)
            try:
                print("Recognizing...")
                command = r.recognize_google(audio, language='id-ID').lower()
                print(f'You said: {command}')
            except:
                # speak(random.choice(Cannot_hear_RES))
                print('Please try again')
                command = self.mic_input()
            return command
        except Exception as e:
            print(e)
            return  False

    def tts(self, text):
        """
        Convert any text to speech
        :param text: text(String)
        :return: True/False (Play sound if True otherwise write exception to log and return  False)
        """
        try:
            engine.say(text)
            engine.runAndWait()
            engine.setProperty('rate', 175)
            return True
        except:
            t = "Sorry I couldn't understand and handle this input"
            print(t)
            return False
    
    def tell_me_date(self):
        return date_time.date()

    def tell_time(self):

        return date_time.time()
        
    def website_opener(self, domain):
        """
        This will open website according to domain
        :param domain: any domain, example "youtube.com"
        :return: True if success, False if fail
        """
        return website_open.website_opener(domain)
    def web_driver_opener(self, domain):
        """
        This will open website according to domain
        :param domain: any domain, example "youtube.com"
        :return: True if success, False if fail
        """
        return google_search.google_search2(domain)

    def search_anything_google(self, command):
        google_search.google_search(command)
    
    def my_location(self):
        city, state, country = loc.my_location()
        return city, state, country

    def my_alarm(self,command):
        try:
            set_alarm_timer = f"{command}:{'30'}:{'00'}"
            while True:
                now,date,second,set_alarm_timer = alarm_wakeup.alarm(set_alarm_timer)
                sleep(1)
                print("The Set Date is:",now +" "+ set_alarm_timer)
                if now == set_alarm_timer:
                    print("Time to Wake up")
                    winsound.PlaySound("driver/Alarm Clock_alarm.wav",winsound.SND_ASYNC)
                    sleep(10)
                    break
        except Exception as e:
           print("Error "+str(e))
    
    def run_alarm(self,command):
        timeis = time_go.home(command)
        t1 = threading.Thread(target=self.my_alarm, args=(timeis,))
        t1.start()
    
    def tell_me(self, topic):
        return wikipedia.tell_me_about(topic)

    def weather(self, city):
        """
        Return weather
        :param city: Any city of this world
        :return: weather info as string if True, or False
        """
        try:
            res = weather.fetch_weather(city)
        except Exception as e:
            print(e)
            res = False
        return res
    
    def news(self):
        """
        Fetch top news of the day from google news
        :return: news list of string if True, False if fail
        """
        return news.get_news()

    def system_info(self):
        return systems_stats.system_stats()