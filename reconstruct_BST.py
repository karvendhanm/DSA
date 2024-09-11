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


rootNode = BST(10).insert(4).insert(2).insert(1).insert(5).insert(17).insert(19).insert(18)


def preOrderTraversal(node, arr):
    if node is None:
        return

    arr.append(node.value)
    preOrderTraversal(node.left, arr)
    preOrderTraversal(node.right, arr)

    return arr


# first iteration
# O(n log n) time | O(n) space
# O(n) space as we are creating n BST objects.
def reconstructBst(preOrderTraversalValues):
    root = BST(preOrderTraversalValues[0])

    for value in preOrderTraversalValues[1:]:
        root.insert(value)  # log (n) time. BST insertion takes log(n) time.

    return root


preOrderTraversalValues = preOrderTraversal(rootNode, [])
print(reconstructBst(preOrderTraversalValues))
