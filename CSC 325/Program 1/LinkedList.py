# I got all of this code from
# github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Linked%20Lists/SinglyLinkedList.py

# Linked List and Node can be accomodated in separate classes for convenience
from Node import *

class LinkedList(object):
    # Defining the head of the linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # printing the data in the linked list
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

    def add(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        
        if self.tail != None:
            self.tail.next = newNode
            
        self.tail = newNode
    
    # deleting an item based on data(or key)
    def delete(self, data):
        temp = self.head
        # if data/key is found in head node itself
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return
            else:
                #  else search all the nodes
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    prev = temp          #save current node as previous so that we can go on to next node
                    temp = temp.next

                # node not found
                if temp == None:
                    return

                prev.next = temp.next
                return

    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)