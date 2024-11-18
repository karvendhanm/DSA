# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def totNumNodes(head):
    count = 1
    while head.next is not None:
        count += 1
        head = head.next
    return count


def getKthNode(head, n):
    position = 1
    while position != n:
        head = head.next
        position += 1
    return head


# first iteration
# O(n) time | O(1) space
# where n is the number of nodes in the linked list
def removeKthNodeFromEnd(head, k):
    # Write your code here.
    n = totNumNodes(head)
    if n == k:  # denotes the head is to be removed
        # head.next can't be none as there is a at least 2 node guarantee.
        head.value = head.next.value
        head.next = head.next.next
    else:
        kthNode = getKthNode(head, n - k)
        kthNode.next = kthNode.next.next


node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)
node4 = LinkedList(4)

node1.next = node2
node2.next = node3
node3.next = node4

removeKthNodeFromEnd(node1, 3)
print('this is just for debugging')
