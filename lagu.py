import time
from threading import thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_Lyrics(Lyric, delay, speed):
    time.sleep(delay)
    animate_text

def sing_song():
lyrics = [
    ("ceeeriiitaa kita tak jauh berbeda", 7.25 )
    ("Got beat down by the world", 2.59)
    ("Sometimes i wanna fold", 2.42)
    ("Namun suratmu kan kuceritakan" 3.02)
    ("ke anak anakku nanti", 3.20)
    ("bahwa aku pernah dicintai", 4.31)
]