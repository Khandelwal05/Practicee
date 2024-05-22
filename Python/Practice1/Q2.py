class Shape:
    def area(self):
        pass
    
class circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def circle_area(self):
        area=3.14*self.radius*self.radius
        print("Area of circle is ", area)

class rectangle(Shape):
    def __init__(self, l,b):
        self.l=l
        self.b=b
    def rectangle_area(self):
        area=self.l*self.b
        print("Area of rectangle is ", area)

class triangle (Shape):
    def __init__(self, b,h):
        self.b=b
        self.h=h
    def triangle_area(self):
        area=0.5*self.b*self.h
        print("area of triangle is ", area)

        
S1=circle(2)
S1.circle_area()

S2=rectangle(2,4)
S2.rectangle_area()

S3=triangle(2,6)
S3.triangle_area()