'''Define a class named Rectangle which inherits from Shape class from task 2. 
Class instance can be constructed by a length and width. 
The Rectangle class has a method which can compute the area'''


class Shape:
    def __init__(self, length):
        pass


    def shape_area(self):
        print(0)
        return 0


class Rectangle(Shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width


    def compute_area(self):
        area = self.length*self.width
        print(area)


a = float(input())
b = float(input())
x = Rectangle(a,b)
x.compute_area()
