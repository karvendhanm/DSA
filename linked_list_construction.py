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

    # O(1) time and O(1) space
    def setHead(self, node):
        # Write your code here.
        self.remove(node)
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node

    # O(1) time and O(1) space
    def setTail(self, node):
        # Write your code here.
        self.remove(node)
        node.prev = self.tail
        node.next = None
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node

    # O(1) time and O(1) space
    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        self.remove(nodeToInsert)
        if node == self.head:
            self.setHead(nodeToInsert)
            return

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) time and O(1) space
    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        self.remove(nodeToInsert)
        if node == self.tail:
            self.setTail(nodeToInsert)
            return

        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # O(p) time and O(1) space
    # where p is the given position where node is to be inserted
    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
            return

        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # O(n) time and O(1) space
    # n is the number of nodes in the linked list.
    def removeNodesWithValue(self, value):
        # Write your code here.
        currentNode = self.head
        while currentNode is not None:
            nextNode = currentNode.next
            if currentNode.value == value:
                self.remove(currentNode)
            currentNode = nextNode

    # O(1) time and O(1) space
    def remove(self, node):
        # Write your code here.
        if self.head == node:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

        if self.tail == node:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.next = node.prev = None

    # O(n) time and O(1) space
    # n is the number of nodes in the linked list.
    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

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
# doubleLinkedList.head = node1
# doubleLinkedList.tail = node5
doubleLinkedList.setHead(node6)
print('this is just for debugging')
