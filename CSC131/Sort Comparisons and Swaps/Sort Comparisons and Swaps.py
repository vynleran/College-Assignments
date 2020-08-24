######################################################################################################################
# Name: Parsa Jahanlou
# Date: Due June 11th, 2020
# Description: Swaps and Comparisons 
######################################################################################################################

# creates the list
def getList():
   return [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]
#   return [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]
#   return [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]
#   return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#   return [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]

# the bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def bubbleSort():
    userList = getList()
    n = len(userList)
    comparison = 0
    swap = 0
    print "Before the bubble sort, list = {}.".format(userList)
    for i in range(1, n):
        for j in range(1, n - i + 1):
            comparison += 1
            if (userList[j] < userList[j - 1]):
                temp = userList[j]
                swap += 1
                userList[j] = userList[j - 1]
                userList[j -1] = temp
    print ("After the bubble sort, list = {}.".format(userList))
    print ("Amount of comparisons are: {}. Amount of swaps are {}.".format(comparison, swap))
    print
    
# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def optimizedBubbleSort():
    userList = getList()
    n = len(userList)
    comparison = 0
    swap = 0
    print ("Before the optimized bubble sort, list ={}".format(userList))
    for i in range(1, n):
        for j in range(1, n - i + 1):
            comparison += 1
            if (userList[j] < userList[j - 1]):
                x = userList
                swap += 1
                temp = userList[j]
                userList[j] = userList[j - 1]
                userList[j - 1] = temp
                if (x == userList):
                    x = swap
                    y = comparison
    print ("After the optimized bubble sort, list = {}".format(userList))
    print ("Amount of comparisons are {}. Amount of swaps are {}".format(y, x))
    print

# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selectionSort():
    userList = getList()
    n = len(userList)
    comparison = 0
    swap = 0
    print ("Before the selection sort, list = {}.".format(userList))
    for i in range(0, n - 1):
        minPosition = i
        for j in range(i + 1, n):
            comparison += 1
            if (userList[j] < userList[minPosition]):
                minPosition = j
        temp = userList[i]
        userList[i] = userList[minPosition]
        swap += 1
        userList[minPosition] = temp
    print ("After the selection sort, list = {}.".format(userList))
    print ("Amount of comparisons are {}. Amount of swaps are {}.".format(comparison, swap))
    print

# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def insertionSort():
    comparison = 0
    swap = 0
    userList = getList()
    n = len(userList)
    i = 1
    print ("Before the insertion sort, list = {}.".format(userList))
    while (i < n):
        comparison += 1
        if (userList[i - 1] > userList[i]):
            comparison += 1
            temp = userList[i]
            j = i - 1
            while (j >= 0 and userList[j] > temp):
                swap += 1
                comparison += 1
                userList[j + 1] = userList[j]
                j = j - 1
            userList[j + 1] = temp
        i += 1
    print ("After the insertion sort, list = {}.".format(userList))
    print ("Amount of comparions are {}. Amount of swaps are: {}.".format(comparison, swap))
    print 

# the main part of the program
bubbleSort()
optimizedBubbleSort()
selectionSort()
insertionSort()
