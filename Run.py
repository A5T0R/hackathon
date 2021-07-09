from Tavern import *
import keyboard
from DrawingTools import clearscreen


def run():

    clearscreen()
    t = Tavern(16,16,"The Dragons Hoard")

    standardtable = Table(4,1)

    t.add(3,3,standardtable)
    t.add(6,6,standardtable)

    t.draw()


if __name__ == "__main__":
 
    run()
    keyboard.wait('q')
