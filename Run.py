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
    vtbl1 = VTable(3,2)
    vtbl2 = VTable(3,2)
    vtbl3 = VTable(3,2)
    vben1 = VBench(3,1)
    vben2 = VBench(3,1)
    vben3 = VBench(3,1)
    vben4 = VBench(3,1)
    vben5 = VBench(3,1)
    vben6 = VBench(3,1)
    htbl = HTable(2,3)
    hben1 = HBench(1,3)
    hben2 = HBench(1,3)
    bar1 = Bar(1,7)
    bar2 = Bar(2,1)
    stl1 = Stool(1,1)
    stl2 = Stool(1,1)
    stl3 = Stool(1,1)
    fpl = Fireplace(1,4)
    dor = Door(3,1)
    sta = Stairs(6,3)
    tvn = Tavern(21,21,"The Dragons Hoard")
    cld = CellarDoor(2,2)
    bro = NPT_BarOwner(1,1,m)
    brs = NPT_BarStaff(1,1,m)
    pat = NPT_Patron(1,1,m)
    ntb = NoticeBoard(2,1)
    vwd1 = VWindow(1,3)
    vwd2 = VWindow(1,3)
    hwd1 = HWindow(3,1)
    hwd2 = HWindow(3,1)
    wal1 = Wall(21,1)
    wal2 = Wall(1,21)
    wal3 = Wall(21,1)
    wal4 = Wall(1,21)
    #chr = Player(1,1,m)

#Furniture
    
    tvn.add( 2,2, vben1 )
    tvn.add( 2,5, vben2 )
    tvn.add( 2,8, vben3 )
    tvn.add( 2,11, vben4 )
    tvn.add( 2,15, vben5 )
    tvn.add( 2,18, vben6 )
    tvn.add( 0,0, wal1 )
    tvn.add( 0,0, wal2 )
    tvn.add( 0,20, wal3 )
    tvn.add( 20,0, wal4 )
    tvn.add( 2,3, vtbl1 )
    tvn.add( 2,9, vtbl2 )
    tvn.add( 2,16, vtbl3 )
    tvn.add( 17,2, bar1 )
    tvn.add( 17,8, bar2 )
    tvn.add( 16,3, stl1 )
    tvn.add( 16,5, stl2 )
    tvn.add( 16,7, stl3 )
    tvn.add( 7,16, hben1)
    tvn.add( 10,16, hben2)
    tvn.add( 8,16, htbl)
    tvn.add( 19,11, fpl)
    tvn.add( 9,0, dor)
    tvn.add( 15,17, sta)
    tvn.add( 18,1, cld)
    tvn.add( 11,20, ntb)
    tvn.add( 0,4, vwd1)
    tvn.add( 0,14, vwd2)
    tvn.add( 4,0, hwd1)
    tvn.add( 14,0, hwd2)
#Character
#    tvn.add( 10,1, chr)
#NPTs

    # tvn.add( 18,5, bro)
    # tvn.add( 8,15, brs)
    # tvn.add( 3,8, pat)
    # tvn.add( 7,16, pat)
    # tvn.add( 16,7, pat)

    m.add(0,0,tvn)
    m.draw()
    return m

def run():

    m = draw_map()

    chr = Player(1,1,m)
    chr.draw(11,3)
    # this will fail... you need to pass an instance of an object with a function called move that takes a single argument keyboard.KeyboardEvent
    bind_movement_keys(chr)

    keyboard.wait("Esc")

if __name__ == "__main__":
 
    run()
