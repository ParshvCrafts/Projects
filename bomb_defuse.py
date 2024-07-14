import random
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # To hide the Pygame introduction message
import pygame
from pygame import mixer   # py -m pip install pygame


def main():
    Clear_and_retrun= "\033c"
    print(Clear_and_retrun)
    print("***💥 Defuse the Bomb 💥***")
    print("You are a Bomb Defuser. Guess the correct wire to defuse [black, red, blue]. If you fail, you have 5 seconds to run away")
    code= random.choice(["black", "red", "blue"])
    enter=input(f"Enter correct wire: ")
    
    if enter==code:
       print(Clear_and_retrun)
       print("Congratulations, bomb successfully defused! ✅ ✅ ✅")
    else:
       n=5
       while n>-1:
         print(Clear_and_retrun)
         print(n)
         time.sleep(1)
         n=n-1
       print("💥💥💥, you lost")
       mixer.init()
       mixer.music.load(r"explosion.mp3") # Download the explosion.mp3 in the same directory to ply the sound
       mixer.music.play()
       while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)

main()
