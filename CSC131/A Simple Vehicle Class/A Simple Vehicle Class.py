######################################################################################################################
# Name: Parsa Jahanlou
# Date: Due 06/16/2020
# Description: A Simple Vehicle Class
######################################################################################################################

# The vehicle class
# The vehicle class inherits the necessary info from the object superclass to allow the accessors and mutators to work
class Vehicle(object):

# a vehicle has a year, make, and model
# constructor so different instances can be made
    def __init__(self, make, model):
        self.make = make
        self.model = model
# every new instance will automatically have 2000 assigned to their year
        self.year = 2000
        
# accesor for the make of the vehicle 
    @property
    def make(self):
        return self._make
# mutator for the make of the vehicle
    @make.setter
    def make(self, vehicleMake):
        self._make = vehicleMake
        
# accesor for model of the vehicle
    @property
    def model(self):
        return self._model
# mutator for the model of the vehicle
    @model.setter
    def model(self, vehicleModel):
        self._model = vehicleModel
        
# accesor for the year of the vehicle
    @property
    def year(self):
        return self._year
# mutator for the year of the vehicle for range checking
    @year.setter
    def year(self, vehicleYear):
        if (vehicleYear not in range(2000, 2020)):
            self._year = self.year
        else:
            self._year = vehicleYear

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
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

