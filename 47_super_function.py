# 47 (04:08:08) super function 🦸

# super() - gives access to the methods & attributes of a parent class
# It returns a temporary object of a parent class when used


""" 
class Rectangle:
    pass

class Square(Rectangle):
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        self.length = length # NOTE: this line is repeated
        self.width = width # NOTE: this line is repeated
        self.height = height 
        
"""


class Rectangle:
    def __init__(self, length, width):
        # attributes common between all children live here
        self.length = length
        self.width = width


# NOTE: below super() represents a temporary Rectangle class object
# on which attributes & methods are accessible


class Square(Rectangle):
    def __init__(self, length, width):
        # Square accesses attributes shared with its parent (Rectangle) via super
        super().__init__(length, width)

    def area(self):
        return self.length * self.width


class Cube(Rectangle):
    def __init__(self, length, width, height):
        # Cube accesses attributes shared with its parent (Rectangle) via super
        super().__init__(length, width)

        # additional attributes specific to Cube can be added after the call to super()
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


square = Square(3, 3)
print("square.area()", str(square.area()))  # 9

cube = Cube(3, 3, 3)
print("cube.volume()", str(cube.volume()))  # 27
