################################################################################
# Name: Parsa Jahanlou
# Date: Due July 8th, 2020
# Description: Sort Comparisons and Swaps...Reloaded
################################################################################
# Imprtoing plot to be able to graph the comparisons and swaps
from plot import plot

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
   for i in range(n):
      for j in range(0, n - i - 1):
         comparison += 1
         if (userList[j] > userList[j + 1]):
            temp = userList[j]
            swap += 1
            userList[j] = userList[j + 1]
            userList[j + 1] = temp
                                
   # putting the comparisons and swaps in a list 
   bubbleSort = [comparison, swap]
   return bubbleSort
    
# the optimized bubble sort function
# input: a list of integers
# output: a number of comparisons and swaps
def optimizedBubbleSort():
   swap = True 
   userList = getList()
   n = len(userList) - 1
   comparison = 0
   swapCounter = 0
   j = 0
   while (swap == True):
      swap = False
      for i in range(n):
         comparison += 1
         if (userList[i] > userList[i + 1]):
            temp = userList[i]
            userList[i] = userList[i + 1]
            userList[i + 1] = temp
            swap = True
            swapCounter += 1
      n -= 1
      j += 1
                                        
   # putting the comparisons and swaps in a list 
   optimizedSort = [comparison, swapCounter]
   return optimizedSort

# the selection sort function
# input: a list of integers
# output: a number of comparisons and swaps
def selectionSort():
        userList = getList()
        n = len(userList)
        comparison = 0
        swap = 0
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

        # putting the comparisons and swaps in a list 
        selectionSort = [comparison, swap]
        return selectionSort

# the insertion sort function
# input: a list of integers
# output: a number of comparisons and swaps
def insertionSort():
        comparison = 0
        swap = 0
        userList = getList()
        n = len(userList)
        i = 1
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
                
        # putting the comparisons and swaps in a list        
        insertionSort = [comparison, swap]
        return insertionSort 

# the main part of the program
bubble = bubbleSort()
optimized = optimizedBubbleSort()
selection = selectionSort()
insertion = insertionSort()
plot(bubble, optimized, selection, insertion)


