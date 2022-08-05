from random import randint

class Die():
    '''Class representing a single die'''

    def __init__(self, nr_sides):
        self.nr_sides = nr_sides

    def roll(self):
        '''Return a figure between 1 and 6'''
        return randint(1,self.nr_sides)
    