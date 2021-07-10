from DrawingTools import *

from collections import namedtuple

class Tavern:

    def __init__(self, w, h, n):
        self.w = w
        self.h = h
        self.name = n
        self.objects = []

    def draw(self,anchor_x,anchor_y):
        draw_box( anchor_x, anchor_y, self.w, self.h, 'W', Fore.RED, Back.WHITE, False )

        for lo in self.objects:
            lo.object.draw(anchor_x + lo.anchor_x, anchor_y + lo.anchor_y)

        print('%s%s' % (pos(anchor_x*2,self.h+anchor_y+1), self.name), end='\n')


    def add(self,anchor_x,anchor_y,obj):
        LocatedObject = namedtuple('LocatedObject', 'anchor_x anchor_y object')
        self.objects.append(LocatedObject(anchor_x,anchor_y,obj))

    def refresh(self,x,y):
        # actually this thing has the logic to work out if it needs refreshing doesnt it
        for lo in self.objects:
            lo.object.refresh(x,y)