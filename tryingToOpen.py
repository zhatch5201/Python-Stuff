import os
import time
import random

def writeOnDemo():
    y = random.randint(0, 100)
    n = open("C://temp//demofile2.txt", "w+")
    n.write("This won't stop until you kill  the python process:(")
    

def osInteraction():
    os.startfile("C://temp//demofile2.txt")
    time.sleep(0)
    os.system("TASKKILL /F /IM notepad.exe")

def closeAndOpenWriting():
    x = 0
    while x < 10:
        writeOnDemo()
        osInteraction()


closeAndOpenWriting()