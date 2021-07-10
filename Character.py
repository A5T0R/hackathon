from DrawingTools import *

class Player():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, 1, 1, '@', Fore.BLUE, Back.CYAN, False )

class NPT_BarOwner():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, 1, 1, '$', Fore.YELLOW, Back.MAGENTA, False )

class NPT_BarStaff():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, 1, 1, '$', Fore.MAGENTA, Back.YELLOW, False )

class NPT_Patron():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, 1, 1, '&', Fore.MAGENTA, Back.BLACK, False )
