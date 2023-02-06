'''Write the definition of a Point class. Objects from this class should have a
a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points'''

import math
class Point:
    def __init__(self,x,y,x1,y1):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1


    def show(self):
        print("Coordinates of the point:")
        print(self.x,self.y)
        print(self.x1,self.y1)


    def move(self):
        print("Changed coordinates:")
        print(self.y, self.x)
        print(self.y1, self.x1)


    def distance(self):
        print("Distance:")
        print(math.sqrt((self.x - self.x1)**2 + (self.y - self.y1)**2))


x,y = map(int,input().split())
x1,y1 = map(int,input().split())
a = Point(x,y,x1,y1)
a.show()
a.move()
a.distance()