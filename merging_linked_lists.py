class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# first iteration - brute force
# O( n * m) time and O(1) space
# where n in the number of nodes in linkedListOne
# where m is the number of nodes in LinkedListTwo
def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.

    while linkedListOne is not None:
        dummyNode = linkedListTwo
        while dummyNode is not None:
            if linkedListOne == dummyNode:
                return linkedListOne
            dummyNode = dummyNode.next
        linkedListOne = linkedListOne.next
    return None


# second iteration using a set to store the nodes in one of the list
# O(n + m) time and O(n) space
# where n is the number of nodes in linkedListOne
# where m is the number of nodes in linkedListTwo
def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    set1 = set()
    while linkedListOne is not None:
        set1.add(linkedListOne)
        linkedListOne = linkedListOne.next

    while linkedListTwo is not None:
        if linkedListTwo in set1:
            return linkedListTwo
        linkedListTwo = linkedListTwo.next

    return None


def getNumberOfNodes(linkedList):
    count = 0
    while linkedList is not None:
        count += 1
        linkedList = linkedList.next
    return count

# third iteration
# O(n + m) time and O(1) space
# where n is the number of nodes in linkedListOne
# where m is the number of nodes in linkedListTwo
def mergingLinkedLists(linkedListOne, linkedListTwo):
    count1 = getNumberOfNodes(linkedListOne)
    count2 = getNumberOfNodes(linkedListTwo)

    biggerLinkedList = linkedListOne if count1 >= count2 else linkedListTwo
    smallerLinkedList = linkedListTwo if count1 >= count2 else linkedListOne

    diff = abs(count1 - count2)
    while diff:
        biggerLinkedList = biggerLinkedList.next
        diff -= 1

    while biggerLinkedList and smallerLinkedList:
        if biggerLinkedList == smallerLinkedList:
            return biggerLinkedList
        biggerLinkedList = biggerLinkedList.next
        smallerLinkedList = smallerLinkedList.next
    return None


# fourth iteration
# O(n + m) time and O(1) space
# where n is the number of nodes in linkedListOne
# where m is the number of nodes in linkedListTwo
def mergingLinkedLists(linkedListOne, linkedListTwo):

    dummyNodeOne = linkedListOne
    dummyNodeTwo = linkedListTwo
    while dummyNodeOne is not dummyNodeTwo:
        if not dummyNodeOne:
            dummyNodeOne = linkedListTwo
        else:
            dummyNodeOne = dummyNodeOne.next

        if not dummyNodeTwo:
            dummyNodeTwo = linkedListOne
        else:
            dummyNodeTwo = dummyNodeTwo.next
    return dummyNodeOne



node11 = LinkedList(2)
node12 = LinkedList(4)
node13 = LinkedList(7)
node14 = LinkedList(1)

node11.next = node12
node12.next = node13
node13.next = node14

node21 = LinkedList(9)

tmp = mergingLinkedLists(node11, node21)

