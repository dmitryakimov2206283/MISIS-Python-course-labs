from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    @property
    def X(self):
        return self._X
    
    @property
    def Y(self):
        return self._Y

    @X.setter
    def X(self, value):
        self._X = value

    @Y.setter
    def Y(self, value):
        self._Y = value

    def __add__(self, other):
        new_x = self.X + other.X
        new_y = self.Y + other.Y
        return Vector(new_x, new_y)
    
    def __sub__(self, other):
        new_x = self.X - other.X
        new_y = self.Y - other.Y
        return Vector(new_x, new_y)
    
    def __mul__(self, other):
        return self.X * other.X + self.Y * other.Y
    
    def __len__(self):
        return int(sqrt(self.X * self.X + self.Y * self.Y))
    
    def __eq__(self, other):
        return len(self) == len(other)
    
    def __ne__(self, other):
        return len(self) != len(other)
    
    def __lt__(self, other):
        return len(self) < len(other)
    
    def __le__(self, other):
        return len(self) <= len(other)
    
    def __gt__(self, other):
        return len(self) > len(other)
    
    def __ge__(self, other):
        return len(self) >= len(other)
    
    def __str__(self):
        return f"<{self.X}, {self.Y}>"
    

v1 = Vector(3, 5)
v2 = Vector(8, 1)

print(f"Sum: {v1 + v2}")
print(f"Substraction: {v1 - v2}")
print(f"Multiplication: {v1 * v2}")

print(f"v1 = v2: {v1 == v2}")
print(f"v1 != v2: {v1 != v2}")
print(f"v1 > v2: {v1 > v2}")
print(f"v1 < v2: {v1 < v2}")
print(f"v1 >= v2: {v1 >= v2}")
print(f"v1 <= v2: {v1 <= v2}")