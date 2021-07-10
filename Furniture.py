from DrawingTools import *

class VTable():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 3, 1, 'C', Fore.BLUE, Back.GREEN, True )
        draw_box( anchor_x, anchor_y +1, 3, 2, 'T', Fore.GREEN, Back.BLUE, True )
        draw_box( anchor_x, anchor_y +3, 3, 1, 'C', Fore.BLUE, Back.GREEN, True )

class HTable():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 1, 3, 'C', Fore.BLUE, Back.GREEN, True )
        draw_box( anchor_x +1, anchor_y, 2, 3, 'T', Fore.GREEN, Back.BLUE, True )
        draw_box( anchor_x +3, anchor_y, 1, 3, 'C', Fore.BLUE, Back.GREEN, True )

class Bar():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 1, 6, 'B', Fore.MAGENTA, Back.YELLOW, True )
        draw_box( anchor_x, anchor_y +6, 2, 1, 'B', Fore.MAGENTA, Back.YELLOW, True )

class Stool():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 1, 1, 'S', Fore.BLACK, Back.RED, True )


class Fireplace():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 1, 4, 'F', Fore.RED, Back.CYAN, True )
        
class Stairs():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 6, 3, 'I', Fore.RED, Back.MAGENTA, True )

class Door():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 3, 1, 'D', Fore.BLACK, Back.BLUE, True )  

class HWindow():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 3, 1, 'W', Fore.CYAN, Back.BLUE, True ) 

class VWindow():


    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 1, 3, 'W', Fore.CYAN, Back.BLUE, True ) 

class NoticeBoard():


    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 2, 1, 'N', Fore.BLACK, Back.YELLOW, True ) 

class CellarDoor():

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 2, 2, 'O', Fore.BLACK, Back.GREEN, True)

