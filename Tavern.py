from DrawingTools import *

from collections import namedtuple

class Tavern:

    def __init__(self, w, h, n):
        self.anchor_x = 1
        self.anchor_y = 1
        self.w = w
        self.h = h
        self.name = n
        self.objects = []

    def draw(self):
        draw_box( self.anchor_x, self.anchor_y, 16, 16, 'W', Fore.RED, Back.WHITE, False )

        for lo in self.objects:
            lo.object.draw(self.anchor_x + lo.anchor_x, self.anchor_y + lo.anchor_y)

        print(self.name)

    def add(self,anchor_x,anchor_y,obj):
        LocatedObject = namedtuple('LocatedObject', 'anchor_x anchor_y object')
        self.objects.append(LocatedObject(anchor_x,anchor_y,obj))

