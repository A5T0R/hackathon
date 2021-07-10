from DrawingTools import *

class Table():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 3, 1, 'C', Fore.BLUE, Back.GREEN, True )
        draw_box( anchor_x, anchor_y +1, 3, 2, 'T', Fore.GREEN, Back.BLUE, True )
        draw_box( anchor_x, anchor_y +3, 3, 1, 'C', Fore.BLUE, Back.GREEN, True )

class Bar():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 2, 1, 'B', Fore.MAGENTA, Back.YELLOW, True )
        draw_box( anchor_x, anchor_y +1, 1, 4, 'B', Fore.MAGENTA, Back.YELLOW, True )

class Stool():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 2, 1, 'S', Fore.BLACK, Back.RED, True )

        