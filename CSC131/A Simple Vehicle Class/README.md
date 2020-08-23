# Program: A Simple Vehicle Class

## Your task in this programming assignment is to write a Python program that implements a simple vehicle class. The class models a vehicle that has a year, a make, and a model (e.g., 2016 Dodge Ram, 2007 Honda Civic, etc). For a 2016 Dodge Ram, for example, the year is 2016, the make is Dodge, and the model is Ram. You will be provided a template that includes code (that you cannot change) in the main part of the program to test the vehicle class:

### ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***

### the main part of the program

v1 = Vehicle("Dodge", "Ram")

v2 = Vehicle("Honda", "Odyssey")

print "v1={} {}".format(v1.make, v1.model)

print "v2={} {}".format(v2.make, v2.model)

print

v1.year = 2016

v2.year = 2016

print "v1={} {} {}".format(v1.year, v1.make, v1.model)

print "v2={} {} {}".format(v2.year, v2.make, v2.model)

print

v1.year = 1999

v2.model = "Civic"

v2.year = 2007

print "v1={} {} {}".format(v1.year, v1.make, v1.model)

print "v2={} {} {}".format(v2.year, v2.make, v2.model)

## This sample code should provide some details of how to structure your vehicle class. Here's what the output of this code with a correctly implemented vehicle class looks like:

v1=Dodge Ram

v2=Honda Odyssey

v1=2016 Dodge Ram

v2=2016 Honda Odyssey

v1=2016 Dodge Ram

v2=2007 Honda Civic

## To help clarify, here are some specifics and/or constraints:

1. The constructor must take two parameters, make and model, and make proper use of mutators to
set these values;

2. By default, a newly instantiated vehicle has a year of 2000;

3. Accessors and mutators (using the decorator method discussed in class) for each instance
variable (i.e., year, make, and model) must be included;

4. A vehicle must have a year that is between 2000 and 2018 inclusive (i.e., implement range
checking so that any other provided value is ignored);

5. You must include a meaningful header, use good coding style, use meaningful variable names,
and comment your source code where appropriate;

6. Your output should be exactly like the sample run shown above; and

7. You must submit your source code as a single .py file.
