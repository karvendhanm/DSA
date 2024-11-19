class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# first iteration
# O(n) time and O(n) space
# where n is the maximum number of nodes in a linked list.
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    quotient = 0
    PermanentLinkedList = NewLinkedList = None
    while linkedListOne is not None or linkedListTwo is not None or quotient > 0:
        firstValue = secondValue = 0
        if linkedListOne:
            firstValue = linkedListOne.value
            linkedListOne = linkedListOne.next

        if linkedListTwo:
            secondValue = linkedListTwo.value
            linkedListTwo = linkedListTwo.next

        currentSum = quotient + firstValue + secondValue
        remainder = currentSum % 10
        quotient = currentSum // 10

        if NewLinkedList:
            NewLinkedList.next = LinkedList(remainder)
            NewLinkedList = NewLinkedList.next
        else:
            NewLinkedList = LinkedList(remainder)
            PermanentLinkedList = NewLinkedList

    return PermanentLinkedList


node11 = LinkedList(2)
node12 = LinkedList(4)
node13 = LinkedList(7)
node14 = LinkedList(1)

node11.next = node12
node12.next = node13
node13.next = node14

node21 = LinkedList(9)
node22 = LinkedList(4)
node23 = LinkedList(5)

node21.next = node22
node22.next = node23

sumOfLinkedLists(node11, node21)
