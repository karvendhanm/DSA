# second iteration
# O(n) time | O(n) space
def minHeightBst(array):

    if not array:
        return None

    center_elm = len(array) // 2
    rootNode = BST(array[center_elm])
    rootNode.left = minHeightBst(array[:center_elm])
    rootNode.right = minHeightBst(array[center_elm + 1:])

    return rootNode


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