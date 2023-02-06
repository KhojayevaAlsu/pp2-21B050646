'''Define a class named Shape and its subclass Square. 
The Square class has an init function which takes a length as argument. 
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.'''

class Shape:
    def __init__(self, length):
        pass


    def shape_area(self):
        return 0

          

class Square(Shape):
    def __init__(self, length):
        self.length = length


    def shape_area(self):
        print(self.length*self.length)

length = float(input())
figure = Square(length)
figure1 = Shape(length)
figure.shape_area()
print(figure1.shape_area())

        
