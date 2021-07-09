from Tavern import *
from Map import *
import keyboard
from DrawingTools import clearscreen


def run():

    clearscreen()

    m = Map()
    t = Tavern(16,16,"The Dragons Hoard")

    t.add(3,3,Table(4,1))

    m.add(5,5,t)

    m.draw()


if __name__ == "__main__":
 
    run()
    keyboard.wait('q')
