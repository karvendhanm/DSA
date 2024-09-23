class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


rootNode = BinaryTree(1)
# left
rootNode.left = BinaryTree(2, parent=rootNode)
rootNode.left.right = BinaryTree(5, parent=rootNode.left)
rootNode.left.right.right = BinaryTree(7, parent=rootNode.left.right)
rootNode.left.right.right.right = BinaryTree(9, parent=rootNode.left.right.right)
rootNode.left.right.right.left = BinaryTree(8, parent=rootNode.left.right.right)
rootNode.left.right.left = BinaryTree(6, parent=rootNode.left.right)
rootNode.left.left = BinaryTree(4, parent=rootNode.left)

# right
rootNode.right = BinaryTree(3, parent=rootNode)


def getLeftMostChild(node):

    currentNode = node
    while currentNode.left:
        currentNode = currentNode.left

    return currentNode


def getRightMostParent(node):

    currentNode = node
    while currentNode.parent is not None and currentNode == currentNode.parent.right:
        currentNode = currentNode.parent

    return currentNode.parent



# third iteration
# utilizing the parent attribute given
# O(h) time | O(1) space
def findSuccessor(tree, node):
    # Write your code here.
    if node.right is not None:
        return getLeftMostChild(node.right)

    return getRightMostParent(node)


obj = findSuccessor(rootNode, rootNode.left.right.right.right)
