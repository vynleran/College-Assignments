######################################################################################################################
# Name: Parsa Jahanlou
# Date: Due July 24th, 2020
# Description: 2D Points...Plotted
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

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas, Point):
    POINT_COLORS = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
    POINT_RADIUS = 0
    # Coordinate class inherits from Point class
    # to instantiate Point instances
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        Point.__init__(self, x=0, y=0)
        self.pack(fill=BOTH, expand=1)

    def plotPoints(self, n):
        for i in range(n):
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            # instantiating a instance from the Point class
            point = Point(x, y)
            self.plot(point)

    def plot(self, point):
        # calling the class variables
        color = self.POINT_COLORS[randint(0, len(self.POINT_COLORS) - 1)]
        self.create_oval(point.x, point.y, point.x + self.POINT_RADIUS * 2, point.y + self.POINT_RADIUS * 2, outline=color)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of points to plot
NUM_POINTS = 5000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
