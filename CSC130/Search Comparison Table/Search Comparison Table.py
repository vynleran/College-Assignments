#######################################################

# Name: Parsa Jahanlou

# Date: Due May 6th, 2020

# Description: Program 5---Search Comparison Table

#######################################################

# importing math to use log

import math

# a function that displays the table

def table(minNum, maxNum, interval):

    print "n             Seq               Bin             Perf"

    print "----------------------------------------------------"

    while (minNum <= maxNum):

        Perf = seq(minNum) / float(binary(minNum))

        Perf = int(round(Perf))

        if (minNum == 0):

            print "{}             {}                {}              {}".format(0, 0, 0, 0)

        elif (minNum > 0):

            print "{}             {}                {}              {}".format(minNum, seq(minNum), binary(minNum), Perf)

        minNum = minNum + interval

# a function that calculates the average number of comparisons of a sequentials search on a list of size n

# -input: the list size

# -output: the average number of comparisons

def seq(minNum):

    return (minNum / 2)

# a function that calculates the average number of comparisons of a sequentials search on a list of size n

# -input: the list size

# -output: the average number of comparisons

def binary(minNum):

    return int((math.log10(minNum + 1) / (math.log10(2))+ 1))

######################################

# MAIN PART OF THE PROGRAM

######################################
# get user input for the minimum (make sure that it is >= 0)

def minimum():

    minNum = input ("Minimum number of list items (>=0)?")

    while minNum < 0:

        print "ERROR: Minimum must be >= 0!"

        minNum = input ("Minimum number of list items (>=0)?")

    return minNum

# get user input for the maximum (make sure that it is >= minimum

def maximum(minNum):

    maxNum = input ("Maximum number of list items (>= min (0))?")

    while maxNum < minNum:

        print "ERROR: Maximum must be >= minimum {}!".format(minNum)

        maxNum = input ("Maximum number of list items (>= min (0))?")

    return maxNum

# get user input for the interval (make sure that it is >= 1)

def userInterval():

    interval = input ("The interval between each row of the table (>= 1)?")

    while interval < 1:

        print "ERROR: Interval must be >= 1!"

        interval = input ("The interval between each row of the table (>= 1)?")

    return interval

# getting the data needed for the table

mini = minimum()

maxi = maximum(mini)

inter = userInterval()

# generate the table

table(mini, maxi, inter)


