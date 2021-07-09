import sys
from DrawingTools import *

class Tavern:

    def __init__(self, w, h, n):
        self.w = w
        self.h = h
        self.name = n

    def draw(self):

        draw_box( 1, 1, 16, 16, 'W', Fore.RED, Back.WHITE, True )
        print(self.name)


        