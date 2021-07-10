from DrawingTools import *

class Player():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, 1, 1, '@', Fore.CYAN, Back.BLUE, False )

class NPT_Barman():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, 1, 1, '$', Fore.YELLOW, Back.MAGENTA, False )