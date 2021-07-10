from DrawingTools import *

class Character:
    def __init__(self, w, h):
        self.w = w
        self.h = h

class Player(Character):

    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, self.w, self.h, '@', Fore.BLUE, Back.CYAN, False )
        self.current_anchor_x = anchor_x
        self.current_anchor_y = anchor_y

    def refresh(self):
        self.draw( self.current_anchor_x, self.current_anchor_y )

    def move(self,event):
        #print(event.name)
        if( event.name == "down" ):
            self.current_anchor_y += 1
        if( event.name == "up" ):
            self.current_anchor_y -= 1
        if( event.name == "left" ):
            self.current_anchor_x -= 1
        if(event.name == "right" ):
            self.current_anchor_x += 1
        self.refresh()
        

class NPT_BarOwner(Character):
    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, self.w, self.h, '$', Fore.YELLOW, Back.MAGENTA, False )

class NPT_BarStaff(Character):
    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, self.w, self.h, '$', Fore.MAGENTA, Back.YELLOW, False )

class NPT_Patron(Character):
    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, self.w, self.h, '&', Fore.MAGENTA, Back.BLACK, False )
