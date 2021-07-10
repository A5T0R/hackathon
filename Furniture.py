from DrawingTools import *

class Furniture:
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.cur_x = 0
        self.cur_y = 0

    def refresh(self,x,y):
        if(x>=self.cur_x and x<(self.cur_x+self.w) and y >= self.cur_y and y < (self.cur_y+self.h)):
            self.draw(self.cur_x,self.cur_y)

class VTable(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 3, 1, 'C', Fore.BLUE, Back.GREEN, True )
        draw_box( anchor_x, anchor_y +1, 3, 2, 'T', Fore.GREEN, Back.BLUE, True )
        draw_box( anchor_x, anchor_y +3, 3, 1, 'C', Fore.BLUE, Back.GREEN, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class HTable(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 1, 3, 'C', Fore.BLUE, Back.GREEN, True )
        draw_box( anchor_x +1, anchor_y, 2, 3, 'T', Fore.GREEN, Back.BLUE, True )
        draw_box( anchor_x +3, anchor_y, 1, 3, 'C', Fore.BLUE, Back.GREEN, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class Bar(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 1, 6, 'B', Fore.MAGENTA, Back.YELLOW, True )
        draw_box( anchor_x, anchor_y +6, 2, 1, 'B', Fore.MAGENTA, Back.YELLOW, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class Stool(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 1, 1, 'S', Fore.BLACK, Back.RED, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y


class Fireplace(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 1, 4, 'F', Fore.RED, Back.CYAN, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y
        
class Stairs(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 6, 3, 'I', Fore.RED, Back.MAGENTA, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class Door(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 3, 1, 'D', Fore.BLACK, Back.BLUE, True )  
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class HWindow(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 3, 1, 'W', Fore.CYAN, Back.BLUE, True ) 
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class VWindow(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 1, 3, 'W', Fore.CYAN, Back.BLUE, True ) 
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class NoticeBoard(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 2, 1, 'N', Fore.BLACK, Back.YELLOW, True ) 
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class CellarDoor(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, 2, 2, 'O', Fore.BLACK, Back.GREEN, True)
        self.cur_x = anchor_x
        self.cur_y = anchor_y

