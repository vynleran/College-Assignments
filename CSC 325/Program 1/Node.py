# I got all of this code from
# github.com/OmkarPathak/Data-Structures-using-Python/blob/master/Linked%20Lists/SinglyLinkedList.py

class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    # function to set data
    def setData(self, data):
        self.data = data

    # function to get data of a particular node
    def getData(self):
        return self.data

    # function to set next node
    def setNext(self, next):
        self.next = next

    # function to get the next node
    def getNext(self):
        return self.next