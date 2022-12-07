# Importing required libraries
from tkinter import *
import datetime
import time
import winsound
from time import sleep

def alarm(set_alarm_timer):
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M:%S")
    date = current_time.strftime("%d/%m/%Y")
    time_delta = datetime.datetime.strptime(set_alarm_timer,'%H:%M:%S') - datetime.datetime.strptime(now,"%H:%M:%S")
    delta_in_seconds = time_delta.total_seconds()
    second = delta_in_seconds
    
    return now,date,second,set_alarm_timer