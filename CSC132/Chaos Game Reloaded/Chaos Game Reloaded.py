######################################################################################################################
# Name: Parsa Jahanlou
# Date: Due August 13th, 2020
# Description: Chaos Game...Reloaded
######################################################################################################################
# Importing the necessary library
from Fractals import *

# ChaosGame class which plots the point on the canvas
class ChaosGame(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)
        self.dimensions = {"min_x": 2, "max_x": WIDTH - 9, "min_y": 2, "max_y": HEIGHT - 9}
        self.dimensions["mid_y"] = (self.dimensions["min_y"] + self.dimensions["max_y"]) / 2
        self.dimensions["mid_x"] = (self.dimensions["min_x"] + self.dimensions["max_x"]) / 2
        self.vertexRadius = 3
        self.vertexColor = "red"
        self.pointRadius = 0
        self.pointColor = "blue"

    def make(self, fractals):
        if (fractals == "SierpinskiTriangle"):
            p1 = SierpinskiTriangle(self.dimensions)
            for vertex in p1.vertices:
                self.plot_point(vertex, self.vertexColor, self.vertexRadius)
            p = p1.vertices[randint(0, len(p1.vertices) - 1)]
            for i in range(p1.num_points):
                p = p.interpt(p1.vertices[randint(0, len(p1.vertices) - 1)], p1.r)
                self.plot_point(p, self.pointColor, self.pointRadius)

        if (fractals == "Pentagon"):
            p1 = Pentagon(self.dimensions)
            for vertex in p1.vertices:
                self.plot_point(vertex, self.vertexColor, self.vertexRadius)
            p = p1.vertices[randint(0, len(p1.vertices) - 1)]
            for i in range(p1.num_points):
                p = p.interpt(p1.vertices[randint(0, len(p1.vertices) - 1)], p1.r)
                self.plot_point(p, self.pointColor, self.pointRadius)

        if (fractals == "Hexagon"):
            p1 = Hexagon(self.dimensions)
            for vertex in p1.vertices:
                self.plot_point(vertex, self.vertexColor, self.vertexRadius)
            p = p1.vertices[randint(0, len(p1.vertices) - 1)]
            for i in range(p1.num_points):
                p = p.interpt(p1.vertices[randint(0, len(p1.vertices) - 1)], p1.r)
                self.plot_point(p, self.pointColor, self.pointRadius)

        if (fractals == "Octagon"):
            p1 = Octagon(self.dimensions)
            for vertex in p1.vertices:
                self.plot_point(vertex, self.vertexColor, self.vertexRadius)
            p = p1.vertices[randint(0, len(p1.vertices) - 1)]
            for i in range(p1.num_points):
                p = p.interpt(p1.vertices[randint(0, len(p1.vertices) - 1)], p1.r)
                self.plot_point(p, self.pointColor, self.pointRadius)

        if (fractals == "SierpinskiCarpet"):
            p1 = SierpinskiCarpet(self.dimensions)
            for vertex in p1.vertices:
                self.plot_point(vertex, self.vertexColor, self.vertexRadius)
            p = p1.vertices[randint(0, len(p1.vertices) - 1)]
            for i in range(p1.num_points):
                p = p.interpt(p1.vertices[randint(0, len(p1.vertices) - 1)], p1.r)
                self.plot_point(p, self.pointColor, self.pointRadius)

    def plot_point(self, point, color, radius):
        self.create_oval(point.x, point.y, point.x + 2 * radius, point.y + 2 * radius, outline=color, fill=color)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520

# the implemented fractals
FRACTALS = [ "SierpinskiTriangle", "SierpinskiCarpet",\
 "Pentagon", "Hexagon", "Octagon" ]

# create the fractals in individual (sequential) windows
for f in FRACTALS:
    window = Tk()
    window.geometry("{}x{}".format(WIDTH, HEIGHT))
    window.title("The Chaos Game...Reloaded")
    # create the game as a Tkinter canvas inside the window
    s = ChaosGame(window)
    # make the current fractal
    s.make(f)
    # wait for the window to close
    window.mainloop()
