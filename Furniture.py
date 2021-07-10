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
        draw_box( anchor_x, anchor_y, self.w, self.h, 'T', Fore.GREEN, Back.BLUE, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class VBench(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h, 'C', Fore.BLUE, Back.GREEN, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class HTable(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h, 'T', Fore.GREEN, Back.BLUE, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class HBench(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h, 'C', Fore.BLUE, Back.GREEN, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class Bar(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h, 'B', Fore.MAGENTA, Back.YELLOW, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class Stool(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h ,'S', Fore.BLACK, Back.RED, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y


class Fireplace(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h ,'F', Fore.RED, Back.CYAN, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y
        
class Stairs(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h ,'I', Fore.RED, Back.MAGENTA, True )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class Door(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h ,'D', Fore.BLACK, Back.BLUE, True )  
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class HWindow(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h ,'W', Fore.CYAN, Back.BLUE, True ) 
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class VWindow(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h ,'W', Fore.CYAN, Back.BLUE, True ) 
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class NoticeBoard(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h ,'N', Fore.BLACK, Back.YELLOW, True ) 
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class CellarDoor(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h ,'O', Fore.BLACK, Back.GREEN, True)
        self.cur_x = anchor_x
        self.cur_y = anchor_y

class Wall(Furniture):

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h, 'W', Fore.RED, Back.WHITE, False )
        self.cur_x = anchor_x
        self.cur_y = anchor_y