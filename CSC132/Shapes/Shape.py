######################################################################################################################
# Name: Parsa Jahanlou
# Date: Due August 7th, 2020
# Description: Shapes
######################################################################################################################

# shape class which acts as the superclass
class Shape(object):
    def __init__(self, height=1, width=1):
        # instance variables
        self.height = height
        self.width = width

    # getter and setter for height
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        # range checking
        if(value <= 0):
            self._height = 1
        elif (value < 0):
            self._height = self.height
        else:
            self._height = value

    # getter and setter for width
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        # range checking
        if (value == 0):
            self._width = 1
        elif (value < 0):
            self._width = self.width
        else:
            self._width = value

    # magic function for returning the instances
    def __str__(self):
        string = ""
        for i in range(self.width):
            print("* " * self.height)
        return string

# rectangle class
class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)

# square class
class Square(Shape):
    def __init__(self, height):
        super().__init__(height, height)

# triangle class
class Triangle(Shape):
    def __init__(self, height):
        super().__init__(height, height)

    # magic function for returning the triangle instances
    def __str__(self):
        string = ""
        for i in range(self.width):
            print("* " * (self.width - i))
        return string


# parallelogram class
class Parallelogram(Shape):
    def __init__(self, height, width):
        super().__init__(height, width)

    # magic function for returning parallelogram instances
    def __str__(self):
        string = ""
        for i in range(self.width):
                print("  " * (self.width-(i+1)) + "* " * (self.height))
        return string

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create and display several shapes
r1 = Rectangle(12, 4)
print(r1)
s1 = Square(6)
print(s1)
t1 = Triangle(7)
print(t1)
p1 = Parallelogram(10, 3)
print(p1)
r2 = Rectangle(0, 0)
print(r2)
p1.width = 2
p1.width = -1
p1.height = 2
print(p1)