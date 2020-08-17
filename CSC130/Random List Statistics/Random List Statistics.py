#############################################
# Name: Parsa Jahanlou
# Date: Due May 18th, 2020
# Description: Random List Statistics
#############################################
from random import randint
# Function that prompts the user for a list size, minimum, and maximum values, creates the list, and returns it
# you must use the list functions discussed in class to add integers to the list
def fillList():
    userList = []
    listSize = input ("How many random integers would you like to add to the list?")
    maximum = input ("What would you like the maximum to be?")
    minimum = input ("What would you like the minimum to be?")
    for numbers in range(1, listSize + 1):
        randomNums = randint(minimum, maximum)
        userList.append(randomNums)
    return userList
# Functions that receives the list as parameters, and calculates and returns the mean
def meanList(nums):
    sumList = 0
    counter  = 0
    while counter < len(nums):
        sumList = sumList + nums[counter]
        mean = sumList / float(len(nums))
        counter += 1
    return mean
# Function that receives the list as parameters, and calculates and returns the median
def medianList(nums):
    nums.sort()
    if (len(nums) % 2 == 0):
        median = float((nums[(len(nums) / 2)] + nums[(len(nums) / 2) + 1]) / 2)
        return median
    elif (len(nums) % 2 == 1):
        median = nums[len(nums) / 2]
        return median
# Function that receives the list as parameters, and calculates and returns the range 
def rangeList(nums):
    nums.sort()
    range_list = nums[len(nums) - 1] - nums[0]
    return range_list
################################################
# MAIN PART OF THE PROGRAM
# implement the main part of your program below
# comments have been added to assist you
################################################
# creates the list
nums = fillList()
print "The list: {}".format(nums)
# calculate and display the mean
mean = meanList(nums)
print "The mean of the list is {}.".format(mean)
# calculate and display the median
median = medianList(nums)
print "The median of the list is {}.".format(median)
# calculates and display the range
range_list = rangeList(nums)
print "The range of the list is {}.".format(range_list)


        
