from colorama import *
import colorama
import os

colorama.init()

def pos(x,y):
    return Cursor.POS(x, y)

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_box( x_anchor, y_anchor, width, height, letter, back_colour, fore_colour, solid ):
        doubleletter = letter+letter
        print(back_colour, end='')
        print(fore_colour, end='')
        print('%s%s' % (pos(x_anchor, y_anchor), letter*width*2), end='')
        for y in range(1, height):
            if solid:
                print('%s%s' % (pos(x_anchor, y), letter*width*2), end='')
            else:
                print('%s%s%s%s' % (pos(1, y),letter + letter,pos((width*2)-1, y), letter + letter), end='')
        print('%s%s' % (pos(1, height), letter*width*2), end='')
        print(pos(1,height+2))
        print(Back.BLACK, end='')
        
