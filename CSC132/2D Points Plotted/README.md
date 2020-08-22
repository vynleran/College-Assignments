# Program: 2D Points...Plotted

Using the template provided on the class web site, your task in this programming assignment is to implement a coordinate system class using the Tkinter Python library that will enable plotting points graphically. Clearly, you will need to re-implement the 2D point class from the previous programming assignment (since you will be plotting instances of points!).

## First, re-implement your 2D point class. Recall the requirements:

- A 2D point is made up of an x-component and a y-component. Each component is a floating
point value;

- A constructor should initialize a point either with specified values for the x- and y-components or
the point (0.0,0.0) as default;

- Instance variables should be appropriately named (i.e., beginning with underscores);

- Accessors and mutators should provide read access of and write access to the instance variables;

- A function named dist should take two points as input and calculate and return the floating
point distance between the two points;

- A function named midpt should take two points as input and calculate and return the
midpoint of the two points; and

- A magic function should provide a string representation of a point in the format (x,y).

## Second, implement the coordinate system class. Note the following requirements:

- The coordinate system class must inherit from Tkinter's canvas class and fill the entire window
(except for the title bar);

- A function named plotPoints should take the number of points to plot as input (set to
5,000 by default in the main part of the program), and plot that many points to the canvas;

- Plotted points should be individual instances of your 2D point class, each with random x- and ycomponents that are within the width and height of the canvas (set to 800x800 by default in
the main part of the program);

- Plotted points should have a radius of 0 (i.e., a point is made up of a single pixel);

- Points should be plotted in a random color from the following set of colors: black, red, green,
blue, cyan, yellow, and magenta;

- The coordinate system class must include class variables for point radius and point colors –
that are referred to as appropriate within the class; and

- You are free to define other functions in the coordinate system class as appropriate (e.g., a plot
function that plots a single point of a specified radius in a specified color).

## To help clarify, here are some specifics and/or constraints:

1. Make sure that your 2D point class addresses all of the requirements listed above (note that a
properly implemented 2D point class in the last programming assignment ensures this);

2. Make sure that your coordinate system class addresses all of the requirements listed above;

3. You must include a meaningful header, use good coding style, use meaningful variable names,
and comment your source code where appropriate;

4. Your output should look somewhat like the sample run shown above; and

5. You must submit your source code as a single .py file.
