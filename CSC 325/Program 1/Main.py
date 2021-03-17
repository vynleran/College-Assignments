from LinkedList import *
import os.path
from os import path

# Getting the user file
userFile = input('File name: ')

# if the user enters the wrong file
inDir = False
while not inDir:
    if(os.path.exists(userFile)):
        inDir = True
    else:
        print('file not found!')
        print()
        userFile = input('File Name: ')

# Sending the file into python
fileOne = open(userFile, 'r')

# creating a LL instance
ll = LinkedList()

# going through the file and inserting chars to the LL
while True: 
    # read by character 
    char = fileOne.read(1)           
    if not char:  
        break
          
    ll.insert(char) 

print(ll.size())

# getting the user input
userInput = input('Pattern: ')

# next implement the algorithms in the linkedlist class
    # put something in them to estimate the time
# call those here and print the outputs
  
fileOne.close()

# brute force in the main
def brute(ll, pattern):
    count = 0
    patternLength = len(pattern)
    llLength = ll.size()
    for i in range(stringLength):   # going through the LinkedList
        if string[i:patternLength + i] == pattern:  # finding the match
            count += 1
    
    return count