import sys
from DrawingTools import *

class Tavern:

    def __init__(self, w, h, n):
        self.w = w
        self.h = h
        self.name = n

    def draw(self):
        print(Back.WHITE, end='')
        print(Fore.RED, end='')
        print('%s%s' % (pos(1, 1), 'W'*self.w*2), end='')
        for y in range(1, self.h):
            print('%s%s%s%s' % (pos(1, y),'WW',pos((self.w*2)-1, y), 'WW'), end='')
        print('%s%s' % (pos(1, self.h), 'W'*self.w*2), end='')
        print(pos(1,self.h+2))
        print(Back.BLACK, end='')
        print(f'{self.name}')


        