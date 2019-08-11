import os

def myPasswordNow():
    os.system("net user Administrator *")
    os.system("password")
    os.system("password")

myPasswordNow()