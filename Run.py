from Tavern import *
from Map import *
from Furniture import *
from UserInterface import *
from DrawingTools import clearscreen
import time


def draw_map():

    clearscreen()

    m = Map()

    vtbl = VTable(4,1)
    htbl = HTable(1,4)
    bar = Bar(2,5)
    stl = Stool(1,1)
    fpl = Fireplace(1,3)
    dor = Door(2,1)
    sta = Stairs(4,2)
    tvn = Tavern(20,20,"The Dragons Hoard")
    cld = CellarDoor(1,1)

    tvn.add( 2,2, vtbl )
    tvn.add( 2,8, vtbl )
    tvn.add( 2,14, vtbl)
    tvn.add( 16,2, bar )
    tvn.add( 15,3, stl )
    tvn.add( 15,5, stl )
    tvn.add( 15,7, stl )
    tvn.add( 7,15, htbl)
    tvn.add( 18,11, fpl)
    tvn.add( 9,0, dor)
    tvn.add( 14,16, sta)
    tvn.add( 17,1, cld)

    m.add(0,0,tvn)
    m.draw()

def run():

    draw_map()

    # this will fail... you need to pass an instance of an object with a function called move that takes a single argument keyboard.KeyboardEvent
    bind_movement_keys()

    keyboard.wait("Esc")

if __name__ == "__main__":
 
    run()
