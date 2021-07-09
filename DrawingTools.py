from colorama import *
import colorama
import os

colorama.init()

def pos(x,y):
    return Cursor.POS(x, y)

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')