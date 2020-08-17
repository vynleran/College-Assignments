##################################################
# Name: Parsa Jahanlou
# Date: April 19th, 2020
# Description: Program 3 --- Casual Statistics
##################################################
def users_int():
    return input("Enter an integer: ")
# Function that prompts the user to enter an integer and returns it
def max_int(num_1, num_2, num_3):
    values = [num_1, num_2, num_3]
    values.sort()
    max = values[-1]
    print ("The maximum value is {}".format(max))
    return max
# Functions that receives three integers as parameters, and calculates and returns the maximum 
def min_int(num_1, num_2, num_3):
    values = [num_1, num_2, num_3]
    values.sort()
    min = values[0]
    print ("The minimum value is {}".format(min))
    return min
# Functions that receives three integers as parameters, and calculates and returns the minimum
def mean(num_1, num_2, num_3):
    print "The mean is {}".format((num_1 + num_2 + num_3)/3)
    return mean
# Functions that receives three integers as parameters, and calculates and returns the mean
def median(num_1, num_2, num_3):
    [num_1, num_2, num_3].sort()
    print ("The median is {}".format([num_1, num_2, num_3][1]))
    return median
# Functions that receives three integers as parameters, and calculates and returns the median
def mode(num_1, num_2, num_3):
    if num_1 == num_2:
        print "The mode is {}".format(num_1)
    elif num_1 == num_3:
        print "The mode is {}".format(num_1)
    elif num_2 == num_3:
        print "The mode is {}".format(num_2)
    else:
        print "The mode is undefined."
    return mode
# Functions that receives three integers as parameters, and calculates and returns the mode
def range_ints(num_1, num_2, num_3):
    values = [num_1, num_2, num_3]
    values.sort()
    min = values[0]
    max = values[2]
    print ("The range is {}".format(max - min))
    return range_ints
# Functions that receives three integers as parameters, and calculates and returns the range
########################################
# Main part of the program
# Implement the main part of your program below
# Comments have been added to assist you
########################################
num_1 = users_int()
num_2 = users_int()
num_3 = users_int()
# get three integers from the user
min_int(num_1, num_2, num_3)
# determine and display the minimum value
max_int(num_1, num_2, num_3)
# determine and display the maximum value
mean(num_1, num_2, num_3)
# calculate and display the mean
median(num_1, num_2, num_3)
# calculate and display the median
mode(num_1, num_2, num_3)
# calculate and display the mode
range_ints(num_1, num_2, num_3)
# calculate and display the range

