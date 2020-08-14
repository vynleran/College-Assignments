######################################################################################################################
# Name: Parsa Jahanlou
# Date: Due August 3rd, 2020
# Description: Chaos Game
######################################################################################################################
# Importing the necessary library
import math
from tkinter import *
from random import randint

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


class Chaos(Canvas, Point):
    # The suggested constants
    POINT_COLORS = ["blue"]
    VERTIX_COLOR = ["red"]
    POINT_RADIUS = 0
    VERTIX_RADIUS = 3
    # Coordinate class inherits from Point class
    # to instantiate Point instances
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        Point.__init__(self, x=0, y=0)
        self.pack(fill=BOTH, expand=1)

    def plotPoints(self, n):
        v1 = Point(300, 3)
        v2 = Point(5, 510)
        v3 = Point(590, 510)
        verList = [v1, v2, v3]
        self.plotVertix(v1)
        self.plotVertix(v2)
        self.plotVertix(v3)
        p1 = verList[(randint(0, len(verList) - 1))]
        p2 = verList[(randint(0, len(verList) - 1))]
        m = p1.midpt(p2)
        self.plot(m)

        for i in range(n):
            v = verList[(randint(0, len(verList) - 1))]
            mPoint = v.midpt(m)
            self.plot(mPoint)
            m = mPoint

    def plotVertix(self, vertix):
        # calling the class variables
        color = self.VERTIX_COLOR[0]
        self.create_oval(vertix.x, vertix.y, vertix.x + self.VERTIX_RADIUS * 2, vertix.y + self.VERTIX_RADIUS * 2,
                         outline=color, fill=color)

    def plot(self, point):
        # calling the class variables
        color = self.POINT_COLORS[0]
        self.create_oval(point.x, point.y, point.x + self.POINT_RADIUS * 2, point.y + self.POINT_RADIUS * 2, outline=color)


##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
# the number of points to plot
NUM_POINTS = 50000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("Chaos Game")
# create the coordinate system as a Tkinter canvas inside the window
s = Chaos(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
