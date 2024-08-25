import subprocess
import sys

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # To hide the Pygame introduction message
import pygame
from pygame import mixer
import time 

Clear= "\033[2]" # Escape sequence character for clearing the terminal
Clear_and_retrun= "\033c" # Escape sequence character to return cursor to home position to print over
def alarm(seconds):
    time_elpased=0
    
    print(Clear)
    while time_elpased < seconds:
        time.sleep(1)
        time_elpased+= 1 
        
        time_left= seconds-time_elpased
        minutes_left= time_left// 60 # Integer divide which only gives the quotient
        seconds_left= time_left % 60 # Reminder when divided by 60 seconds_left
        
        print(f"{Clear_and_retrun}{minutes_left:02d}:{seconds_left:02d}") #:02d makes the variable 2 digit by adding 0 at front
        
    mixer.init()
    mixer.music.load(r"alarm.mp3") # Download the alarm.mp3 in the same directory to ply the sound
    mixer.music.play()
    time.sleep(4)
    mixer.music.stop()  # wait for music to finish playing
    
time_in= input("Set the Alarm {12:34 format}: ")
minutes= int(time_in.split(":")[0])
seconds= int(time_in.split(":")[1])
total_time= minutes*60 + seconds
alarm(total_time)
