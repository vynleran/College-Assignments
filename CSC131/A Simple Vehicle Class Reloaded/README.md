# Program: A Simple Vehicle Class...Reloaded

## Your task in this programming assignment is to update your previous Python program that implemented a simple vehicle class. Recall that the class models a vehicle that has a year, a make, and a model (e.g., 2016 Dodge Ram, 2007 Honda Civic, etc). This time, you are to add four new classes:

- A truck class that can model various trucks;

- A car class that can model various cars;

- A Dodge Ram class that defines what a Dodge Ram is; and

- A Honda Civic class that defines what a Honda Civic is.

## You will be provided a template that includes code (that you cannot change) in the main part of the program to test the vehicle class:

### DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***

### the main part of the program

ram = DodgeRam(2016)

print ram

civic1 = HondaCivic(2007)

print civic1

civic2 = HondaCivic(1999)

print civic2

## This sample code (along with the class diagram) should provide some details of how to structure your classes. Moreover, comments included in the template should provide further elaboration. Here's what the output of this code with correctly implemented vehicle, truck, car, Dodge Ram, and Honda Civic classes looks like:

Vehicle

Truck Car

DodgeRam HondaCivic

2016 Dodge Ram

2007 Honda Civic

2000 Honda Civic

## Note that a properly structured vehicle class in your previous program won't need to be changed at all! To help clarify, here are some specifics and/or constraints:

1. The vehicle constructor must take two parameters, make and model, and make proper use of
accessors and mutators to get and set these values;

2. By default, a newly instantiated vehicle has a year of 2000;

3. A vehicle must have a year that is between 2000 and 2018 inclusive (i.e., implement range
checking so that any other provided value is ignored);

4. Accessors and mutators (using the decorator method discussed in class) for instance variables
in the vehicle class must be included;

5. The truck and car constructors must take two parameters, make and model, and make proper
use of inheritance to get and set these values;

6. The Dodge Ram and Honda Civic class constructors must take one parameter, year, and make
proper use of inheritance to get and set this value;

7. The Dodge Ram and Honda Civic classes must include appropriate class variables for make and
model;

8. You must include a meaningful header, use good coding style, use meaningful variable names,
and comment your source code where appropriate;

9. Your output should be exactly like the sample run shown above; and

10. You must submit your source code as a single .py file.
