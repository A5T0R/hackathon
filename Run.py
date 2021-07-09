from Tavern import *
import keyboard
from DrawingTools import clearscreen


def run():

    clearscreen()
    t = Tavern(16,16,"The Dragons Hoard")
    t.draw()


if __name__ == "__main__":
 
    run()
    keyboard.wait('q')
