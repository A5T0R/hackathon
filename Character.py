from DrawingTools import *

class Character:
    def __init__(self, w, h, m):
        self.w = w
        self.h = h
        self.map = m

class Player(Character):

    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, self.w, self.h, '@', Fore.BLUE, Back.CYAN, False )
        self.cur_x = anchor_x
        self.cur_y = anchor_y

    def do_move(self, new_x, new_y):
        self.draw( new_x, new_y )

    def move(self,event):
        #print(event.name)
        draw_character( self.cur_x, self.cur_y, self.w, self.h, ' ', Fore.RESET, Back.RESET, False )

        new_x = self.cur_x
        new_y = self.cur_y

        if( event.name == "down" ):
            new_y += 1
        if( event.name == "up" ):
            new_y -= 1
        if( event.name == "left" ):
            new_x -= 1
        if(event.name == "right" ):
            new_x += 1

        if self.map.on_collision_with(new_x,new_y):
            self.map.refresh(self.cur_x,self.cur_y)
            self.do_move(new_x,new_y)
      

class NPT_BarOwner(Character):
    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, self.w, self.h, '$', Fore.YELLOW, Back.MAGENTA, False )

class NPT_BarStaff(Character):
    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, self.w, self.h, '$', Fore.MAGENTA, Back.YELLOW, False )

class NPT_Patron(Character):
    def draw(self,anchor_x,anchor_y):
        draw_character( anchor_x, anchor_y, self.w, self.h, '&', Fore.MAGENTA, Back.BLACK, False )
