from DrawingTools import *

from collections import namedtuple

class Map:

    def __init__(self):
        self.anchor_x = 1
        self.anchor_y = 1
        self.objects = []

    def draw(self):
        for lo in self.objects:
            lo.object.draw(self.anchor_x + lo.anchor_x, self.anchor_y + lo.anchor_y)

    def add(self,anchor_x,anchor_y,obj):
        LocatedObject = namedtuple('LocatedObject', 'anchor_x anchor_y object')
        self.objects.append(LocatedObject(anchor_x,anchor_y,obj))