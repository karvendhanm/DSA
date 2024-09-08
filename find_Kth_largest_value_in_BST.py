class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

        return self


rootNode = BST(5).insert(4).insert(3).insert(6).insert(7)


def findKthLargestValueInBst(tree, k):
    temp = findKthLargestValueInBstHelper(tree, k, [])
    return temp[k-1]



# naive sub-optimal method
# O(n) time | O(n) space
def findKthLargestValueInBstHelper(tree, k, arr):
    # Write your code here.
    if tree is None:
        return None

    findKthLargestValueInBstHelper(tree.right, k, arr)
    arr.append(tree.value)  # constant time operation O(1)
    findKthLargestValueInBstHelper(tree.left, k, arr)

    return arr


print(findKthLargestValueInBst(rootNode, 1))
