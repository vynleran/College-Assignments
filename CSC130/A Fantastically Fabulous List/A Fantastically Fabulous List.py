############################################

# Name: Parsa Jahanlou

# Date: May 11th, 2020

# Description: A Fantastically Fabulous List

############################################

# A function that:

def fillSize():

    theList = []

# (1) prompts the user for a list size

    userSize = input("How many integers would you like to add to this list?")

    counter = 0

    while (counter < userSize):

# (2) prompts the user for the integers to store in the list (corresponding to the list size)

        userNum = input("Enter an integer:")

# (3) creates the list

        theList.append(userNum)

        counter = counter + 1

# (4) returns the list

    return theList

############################################

# MAIN PART OF THE PROGRAM

# implement the maipart of your program below

# comments have been added to assist you

############################################

# create the list

nums = fillSize()

# display information about the list using the list functions discussed in class

print "The original list : {}".format(nums)

print "The length of the list is {}".format(len(nums))

print "The minimum value in the list is {}".format(min(nums))

print "The maximum value in the list is {}".format(max(nums))

nums.reverse()

print "The reversed list: {}".format(nums)

nums.sort()

print "The sorted list: {}".format(nums)



