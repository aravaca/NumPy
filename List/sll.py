class Node:
    def __init__(self, data):
        self.data = data
        self.next = None # like Null in Java

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def insertBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode

    def insertInBetween(self, middle, data):
        newNode = Node(data)
        if self.head is None:
            return
        curr = self.head
        while curr.data is not middle:
            curr = curr.next

        newNode.next = curr.next
        curr.next = newNode
    
    #remove single instance of key
    def remove(self, key):
        if self.head is None:
            return

        curr = self.head
        if curr.next is None:
            if curr.data is key:
                self.head = None
                return
            else:
                return
        
        if curr.data is key:
            self.head = curr.next
            return
        prev = self.head
        while curr:
            if curr.data is key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
                


list = LinkedList()
    
node1 = Node(1)

list.head = node1
list.insertBeginning(2)
list.insertBeginning(3)
list.insertBeginning(4)


list.printList()
list.remove(1)
list.printList()

