##################################
# Name: Parsa Jahanlou
# Date: Due June 8th, 2020
# Description: How Many Zeros?
##################################
from time import time

# This function is basically the algorithm for counting the zeros in each number
def zeroAlgorithm(n, userNum):
    zero = 0
    while (n != 0):
        if (n % 10 == 0):
            zero += 1
        n = n // 10
    return zero

# This function adds the number of zeros in each number to give us the total number of zeros 
def zeroCounter(userNum):
    count = 0
    n = 0
    while (n < userNum):
        n += 1
        zeroNum = zeroAlgorithm(n, userNum)
        count += zeroNum
    print ("The number zeroes written from 1 to {} is {}".format(userNum, count))

# Asking the user for a number to start counting zeros to that number  
userNum = input ("What number do you want to count zeroes to?")
start_time = time()
zeroCounter(userNum)
stop_time = time()
elapsed = stop_time - start_time
print ("This took {} seconds.".format(elapsed))
