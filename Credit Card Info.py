import os
import time

def yourOnlyOption():
    n = open("C://temp//demofile2.txt", "w+")
    n.write("You only have one option." '\n' "Try to restart explorer, make sure that you press the windows key." '\n' "Just kidding, just press ctrl+shift+esc, then click run new task, search for 'explorer.exe' works like a charm")

def revivalOptionReveal():
    os.startfile("C://temp//demofile2.txt")

def broWhyDoYouDoThis():
    os.system("TASKKILL /F /IM explorer.exe")
    os.system("ipconfig /release")
    os.startfile("chrome.exe")

def theWholeShabang():
    yourOnlyOption()
    revivalOptionReveal()
    broWhyDoYouDoThis()

theWholeShabang()