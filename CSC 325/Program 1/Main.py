from LinkedList import *

# Getting the user file
userFile = input('File name: ')

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
          
    ll.add(char) 
    
ll.printLinkedList()

# getting the user input
userInput = input('Pattern: ')

# next implement the algorithms in the linkedlist class
    # put something in them to estimate the time
# call those here and print the outputs

  
fileOne.close()