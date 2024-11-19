class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# first iteration
# O(max(n, m)) time and O(max(n, m)) space
# where n is the length of linkedListOne
# where m is the length of linkedListTwo
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.

    quotient = 0
    currentNode = dummyHead = LinkedList(0)
    while linkedListOne or linkedListTwo or quotient:
        firstValue = linkedListOne.value if linkedListOne else 0
        secondValue = linkedListTwo.value if linkedListTwo else 0

        totalValue = firstValue + secondValue + quotient
        quotient, remainder = divmod(totalValue, 10)

        currentNode.next = LinkedList(remainder)
        currentNode = currentNode.next

        linkedListOne = linkedListOne.next if linkedListOne else None
        linkedListTwo = linkedListTwo.next if linkedListTwo else None

    return dummyHead.next


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
