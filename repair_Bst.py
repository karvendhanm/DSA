class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


root = BST(10)

# left branch
root.left = BST(7)
root.left.left = BST(3)
root.left.right = BST(12)
root.left.left.left = BST(2)

# right branch
root.right = BST(20)
root.right.right = BST(22)
root.right.left = BST(8)
root.right.left.right = BST(14)


# O(n) time | O(h) space
# where n is the number of nodes in the BST
# where h is the height of the BST
def repairBst(tree):
    # Write your code here.
    nodeOne, nodeTwo, previousNode = None, None, None

    def inOrderTraversal(node):
        nonlocal nodeOne, nodeTwo, previousNode
        if node is None:
            return

        inOrderTraversal(node.left)

        if previousNode is not None and previousNode.value > node.value:
            if nodeOne is None:
                nodeOne = previousNode
            nodeTwo = node
        previousNode = node

        inOrderTraversal(node.right)

    inOrderTraversal(tree)
    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
    return tree


# O(n) time | O(h) space
# where n is the number of nodes in the BST
# where h is the height of the BST
# iterative solution
def repairBst(tree):
    # Write your code here.
    nodeOne, nodeTwo, previousNode = None, None, None

    stack = []
    currentNode = tree
    while currentNode is not None or stack:
        while currentNode is not None:
            stack.append(currentNode)
            currentNode = currentNode.left
        currentNode = stack.pop()

        if previousNode is not None and previousNode.value > currentNode.value:
            if nodeOne is None:
                nodeOne = previousNode
            nodeTwo = currentNode
        previousNode = currentNode

        currentNode = currentNode.right
    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
    return tree


print(repairBst(root))

