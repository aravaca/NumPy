class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None # like Null in Java


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.prev = node2
node2.prev = node1

#visualization
currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

currentNode = node3
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("null")