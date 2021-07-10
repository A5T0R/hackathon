from colorama import *
import colorama
import os
import sys

colorama.init()

def pos(x,y):
    return Cursor.POS(x, y)

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_box( x_anchor, y_anchor, width, height, letter, back_colour, fore_colour, solid ):
        doubleletter = letter+letter
        print(back_colour, end='')
        print(fore_colour, end='')
        print('%s%s' % (pos(x_anchor*2, y_anchor), letter*(width*2)), end='')
        for y in range(y_anchor+1, height+y_anchor-1):
            if solid:
                print('%s%s' % (pos(x_anchor*2, y), letter*(width*2)), end='')
            else:
                print('%s%s%s%s' % (pos(x_anchor*2, y),letter + letter,pos(x_anchor*2+(width*2)-2, y), letter + letter), end='')
        print('%s%s' % (pos(x_anchor*2, height+y_anchor-1), letter*(width*2)), end='')
        print(Fore.WHITE, end='')
        print(Back.BLACK, end='')
        print('%s' % pos(44, 24), end='')
        sys.stdout.flush()

def draw_character( x_anchor, y_anchor, width, height, letter, back_colour, fore_colour, solid ):
        doubleletter = letter+letter
        print(back_colour, end='')
        print(fore_colour, end='')
        print('%s%s' % (pos(x_anchor*2, y_anchor), letter*(width*2)), end='')
        for y in range(y_anchor+1, height+y_anchor-1):
            if solid:
                print('%s%s' % (pos(x_anchor*2, y), letter*(width*2)), end='')
            else:
                print('%s%s%s%s' % (pos(x_anchor*2, y),letter + letter,pos(x_anchor*2+(width*2)-2, y), letter + letter), end='')
        print('%s%s' % (pos(x_anchor*2, height+y_anchor-1), letter*(width*2)), end='')
        print(Back.BLACK, end='')
        print('%s' % pos(44, 24), end='')
        
        sys.stdout.flush()