import os
import time
import random
import string

def randomString(stringLength=15):
    #Generate a random string with the combination of lowercase and uppercase letters
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def createNewFile():
    i = 0
    u = input("What would you like to file path to be? use 'C://Users//zacke//desktop//' ")
    f = input("What do you want to call the file? ")
    p = input("What would you like to file extension to be? '.html' '.txt ")
    addContent = input("Would you like to add text/code to this file y/n? ")
    while i < 1:
        if addContent == "y":
            textOnFile = input("What would you like the file to say? ")
            n = open(str(u)+str(f)+str(p), "a+")
            n.write(textOnFile)
            i = 1
        elif addContent == "n":
            n = open(str(u)+str(f)+str(p), "a+")
            n.write(randomString(stringLength=15))
            print("Random content has been added, this will now close.")
            os.startfile(str(u)+str(f)+str(p))
            os.system("TASKKILL /F /IM py.exe")
            i = 1
            
    openTheFile = input("Would you like to open the file you just created y/n? ")
    if openTheFile == "y":
        os.startfile(str(u)+str(f)+str(p))
        os.system("TASKKILL /F /IM py.exe")
    else:
        i = i + 1

def moreFolders():
    x = input("Would you like to create a new file in a folder of your choice y/n? ")
    k = 0
    while k < 1:
        if x == "y":
            y = input("You are about to create more files, are you sure y/n? ")
            if y == "y":
                createNewFile()
                moreFolders()
            elif y == "n":
                print("You said no, process terminated.")
                k = k + 1

        elif x == "n":
            print("You said no, process terminated.")
            k = k + 1
        else:
            moreFolders()

moreFolders()