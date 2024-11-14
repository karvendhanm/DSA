# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        pass

    def setTail(self, node):
        # Write your code here.
        pass

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        pass


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# setting up the next nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# setting up the previous nodes
node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4

doubleLinkedList = DoublyLinkedList()
doubleLinkedList.head = node1
doubleLinkedList.tail = node5

