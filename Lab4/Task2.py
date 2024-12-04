from math import pi

class Figure:
    def area(self):
        pass

class Circle(Figure):
    def __init__(self, r):
        self.R = r

    def __str__(self):
        return f"Circle with area of {self.area()}"

    def area(self):
        return 2 * pi * self.R * self.R

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle wtih area of {self.area()}"

    def area(self):
        return self.height * self.width
    
figures = [
    Circle(2), 
    Rectangle(25, 30), 
    Circle(5), 
    Rectangle(5, 7)
]

for f in figures:
    print(f)