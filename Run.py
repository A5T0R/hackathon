from Tavern import *
from Map import *
from Furniture import *
from UserInterface import *
from DrawingTools import clearscreen
import time
from Character import *


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
    tvn = Tavern(21,21,"The Dragons Hoard")
    cld = CellarDoor(1,1)
    bro = NPT_BarOwner(1,1)
    brs = NPT_BarStaff(1,1)
    pat = NPT_Patron(1,1)
    ntb = NoticeBoard(2,1)
    vwd = VWindow(1,3)
    hwd = HWindow(3,1)

#Furniture
    tvn.add( 2,2, vtbl )
    tvn.add( 2,8, vtbl )
    tvn.add( 2,15, vtbl)
    tvn.add( 17,2, bar )
    tvn.add( 16,3, stl )
    tvn.add( 16,5, stl )
    tvn.add( 16,7, stl )
    tvn.add( 7,16, htbl)
    tvn.add( 19,11, fpl)
    tvn.add( 9,0, dor)
    tvn.add( 15,17, sta)
    tvn.add( 18,1, cld)
    tvn.add( 11,20, ntb)
    tvn.add( 0,4, vwd)
    tvn.add( 0,14, vwd)
    tvn.add( 4,0, hwd)
    tvn.add( 14,0, hwd)
#Character
#    tvn.add( 10,1, chr)
#NPTs

    tvn.add( 18,5, bro)
    tvn.add( 8,15, brs)
    tvn.add( 3,8, pat)
    tvn.add( 7,16, pat)
    tvn.add( 16,7, pat)

    m.add(0,0,tvn)
    m.draw()

def run():

    draw_map()

    chr = Player(1,1)
    chr.draw(10,3)
    # this will fail... you need to pass an instance of an object with a function called move that takes a single argument keyboard.KeyboardEvent
    bind_movement_keys(chr)

    keyboard.wait("Esc")

if __name__ == "__main__":
 
    run()
