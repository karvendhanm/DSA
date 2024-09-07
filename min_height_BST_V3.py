def minHeightBst(array):
    return minHeightBstHelper(array, None, 0, len(array)-1)


# O(n log(n)) time | O(n) space
def minHeightBstHelper(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return

    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]

    if bst is None:
        bst = BST(valueToAdd)                   # O(1) constant time operation
    else:
        bst.insert(valueToAdd)                  # O(log n) time, inserting an element in BST

    minHeightBstHelper(array, bst, startIdx, midIdx-1)
    minHeightBstHelper(array, bst, midIdx+1, endIdx)

    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
minHeightBst(array)
