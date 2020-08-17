#########################################################
# Name: Parsa Jahanlou
# Date: Due June 26th, 2020
# Description: Simple Vehicle Class...Reloaded
#########################################################

# The Vehicle class
# A vehicle has a year, make, and model
# A vehicle is instantiated with a make and model
class Vehicle(object):

    # A vehicle has a year, make, and model
    # Constructor so different instances can be made
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    # Accesor for the make of the vehicle 
    @property
    def make(self):
        return self._make
    # Mutator for the make of the vehicle
    @make.setter
    def make(self, vehicleMake):
        self._make = vehicleMake
        
    # Accesor for model of the vehicle
    @property
    def model(self):
        return self._model
    # Mutator for the model of the vehicle
    @model.setter
    def model(self, vehicleModel):
        self._model = vehicleModel
        
    # Accesor for the year of the vehicle
    @property
    def year(self):
        return self._year
    # Mutator for the year of the vehicle for range checking
    @year.setter
    def year(self, vehicleYear):
        if (vehicleYear not in range(2000, 2020)):
            self._year = 2000
        else:
            self._year = vehicleYear

    # Magic function to return the output in an easier way
    def __str__(self):
        return "{}".format(self.year)
    
# The Truck class
# A truck is a vehicle
# A truck is instantiated with a make and model
class Truck(Vehicle):

    # A Truck class has a make, and model
    # Constructor so different instances can be made
    def __init__(self, make, model, year):
       Vehicle.__init__(self, Truck.make, Truck.model, year)

# The Car class
# A car is a vehicle
# A car is instantiated with a make and model
class Car(Vehicle):

    # A Car class has a make, and model
    # Constructor so different instances can be made
    def __init__(self, make, model, year):
        Vehicle.__init__(self, Car.make, Car.model, year)        

# The Dodge Ram class
# A Dodge Ram is a truck
# A Dodge Ram is instantiated with a year
# All Dodge Rams have the same make and model
class DodgeRam(Truck):

    # Class variables for make and model
    make = "Dodge"
    model = "Ram"
    
    # A Dodge Ram class has a year
    # Constructor so different instances can be made
    def __init__(self, year):
        Truck.__init__(self, DodgeRam.make, DodgeRam.model, year)
    
    # Magic function to return the output in an easier way
    def __str__(self):
        return"{} {} {}".format(Vehicle.__str__(self), DodgeRam.make, DodgeRam.model)

# The Honda Civic class
# A Honda Civic is a car
# A Honda Civic is instantiated with a year
# All Honda Civics have the same make and model
class HondaCivic(Car):

    # Class variables for make and model
    make = "Honda"
    model = "Civic"
    
    # A Honda Civic class has a year
    # Constructor so different instances can be made
    def __init__(self, year):
        Car.__init__(self, HondaCivic.make, HondaCivic.model, year)

    # Magic function to return the output in an easier way
    def __str__(self):
        return"{} {} {}".format(Vehicle.__str__(self), HondaCivic.make, HondaCivic.model)
        
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# The main part of the program
ram = DodgeRam(2016)
print ram

civic1 = HondaCivic(2007)
print civic1

civic2 = HondaCivic(1999)
print civic2

