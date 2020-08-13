######################################################################################################################
# Name: Parsa Jahanlou
# Date: Due July 17th, 2020
# Description: 2D Points
######################################################################################################################
# Importing math library
import math

# The 2D point class
class Point(object):

	# The contructor for Point class
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)

    # The getter for x
    @property
    def x(self):
        return self._x
    # The setter for x
    @x.setter
    def x(self, value):
        self._x = value

    # The getter for y
    @property
    def y(self):
        return self._y
    # The setter for y
    @y.setter
    def y(self, value):
        self._y = value

    # Function for getting the distance between two points
    def dist(self, other):
        xVar = ((other.x - self.x) ** 2)
        yVar = ((other.y - self.y) ** 2)
        equation = xVar + yVar
        distance = math.sqrt(equation)
        return distance

    # Function for getting the midpoint
    def midpt(self, other):
        xVar = (other.x + self.x) / 2
        yVar = (other.y + self.y) / 2
        midpoint = Point(xVar,yVar)
        return midpoint

    # Magic function for printing
    def __str__(self):
        return "({},{})".format(self.x, self.y)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# Create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# Display them
print("p1:", p1)
print("p2:", p2)
print("p3:", p3)
# Calculate and display some distances
print("distance from p1 to p2:", p1.dist(p2))
print("distance from p2 to p3:", p2.dist(p3))
print("distance from p1 to p3:", p1.dist(p3))
# Calculate and display some midpoints
print("midpt of p1 and p2:", p1.midpt(p2))
print("midpt of p2 and p3:", p2.midpt(p3))
print("midpt of p1 and p3:", p1.midpt(p3))
# Just a few more things...
p4 = p1.midpt(p3)
print("p4:", p4)
print("distance from p4 to p1:", p4.dist(p1))
