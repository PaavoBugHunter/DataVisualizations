'''
Randomwalk is a concept for modelling random development of occurrences like consumer purchase confidence in economics.
It has numerous applications in physics, economics, finance, biology, and other disiplines.
'''
from random import choice
'''
Choice-method returns a randomly selected element from a specified sequence.
The sequence can be a string, list, tuple, range of numbers, or any other kind of sequence.
'''
class RWalkGenerator():
    '''Creates an instance of randomwalk (RW) with 500 steps and initial coordinates (0,0)'''
    def __init__(self, num_points = 5000) -> None:
        self.num_points = num_points
        self.x_coordinate = [0]
        self.y_coordinate = [0]

    def fill_walk(self):
        '''Take steps from possible distances and directions in X- and Y-dimensions and add them to RW's location while there are steps left'''
        while len(self.x_coordinate) < self.num_points:
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_coordinate[-1] + x_step
            self.x_coordinate.append(x)

            y = self.y_coordinate[-1] + y_step
            self.y_coordinate.append(y)
