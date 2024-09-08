def minHeightBst(array):
    return minHeightBstHelper(array, 0, len(array) - 1)


# O(n) time | O(n) space
def minHeightBstHelper(array, startIdx, endIdx):
    # avoiding the use of .insert command which adds O(log n) complexity.
    if endIdx < startIdx:
        return

    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])     # O(1) constant time operation

    bst.left = minHeightBstHelper(array, startIdx, midIdx - 1)
    bst.right = minHeightBstHelper(array, midIdx + 1, endIdx)

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
res = minHeightBst(array)
print('this is just for debugging')
