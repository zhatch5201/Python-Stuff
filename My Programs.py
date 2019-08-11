import os
import time
import string
import webbrowser

def openFortnite():
    os.startfile("C://Program Files//Epic Games//Fortnite//FortniteGame//Binaries//Win64//FortniteClient-Win64-Shipping")

def openDiscord():
    os.startfile("C://Users//zacke//AppData//Local//Discord//app-0.0.304//Discord")

def openSpotify():
    os.startfile("C://Users//zacke//AppData//Roaming//Spotify//Spotify")

def openYoutube():
    url1 = "https://www.google.com"
    webbrowser.open(url1)

def openWhat():
    x = input("Would you like to open 1. Fortnite, Spotify, Discord, and Youtube?2. Spotify, Discord, and Youtube? 3. Discord and Youtube?")

    if x == 1:
        openFortnite()
        openDiscord()
        openSpotify()
        openYoutube()
    elif x == 2:
        openSpotify()
        openDiscord()
        openYoutube()
    elif x == 3:
        openDiscord()
        openYoutube()
    else:
        openWhat()

openWhat()