class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, value):
        currentNode = self

        while True:
            if currentNode.next is None:
                currentNode.next = LinkedList(value)
                break
            currentNode = currentNode.next
        return self


treeNode = LinkedList(2).insert(3).insert(7).insert(5).insert(6)

# [2, 3, 7, 5]


# first iteration
# def middleNode(linkedList):
#     # Write your code here.
#     currentNode = linkedList
#     NodeCount = 0
#     while currentNode is not None:
#         NodeCount += 1
#         currentNode = currentNode.next
#
#     for node in range(0, (NodeCount // 2)):
#         linkedList = linkedList.next
#
#     return linkedList


# second iteration
def middleNode(linkedList):

    double_step = linkedList
    single_step = linkedList

    while double_step and double_step.next is not None:
        double_step = double_step.next.next
        single_step = single_step.next

    return single_step
