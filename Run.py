from Tavern import *
from Map import *
from Furniture import *
import keyboard
from DrawingTools import clearscreen


def run():

    clearscreen()

    m = Map()

    tbl = Table(4,1)
    tvn = Tavern(20,20,"The Dragons Hoard")

    tvn.add( 2,2, tbl )
    tvn.add( 2,8, tbl )

    m.add(0,0,tvn)
    m.draw()


if __name__ == "__main__":
 
    run()
    keyboard.wait('q')
