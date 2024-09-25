class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


rootNode = BinaryTree(1)
# left
rootNode.left = BinaryTree(2)
rootNode.left.left = BinaryTree(4)
rootNode.left.right = BinaryTree(5)
rootNode.left.right.left = BinaryTree(7)
rootNode.left.right.right = BinaryTree(8)

# right
rootNode.right = BinaryTree(3)
rootNode.right.right = BinaryTree(6)
rootNode.right.right.left = BinaryTree(9)
rootNode.right.right.left.left = BinaryTree(10)
# rootNode.right.right.right = BinaryTree(10)

class TreeInfo(object):
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height


def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)

    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)

    isBalanced = (abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
                  and leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced)
    height = max(leftSubTreeInfo.height, rightSubTreeInfo.height) + 1
    return TreeInfo(isBalanced, height)


# third iteration
# O(n) time | O(h) space
def heightBalancedBinaryTree(tree):
    # Write your code here.
    return getTreeInfo(tree).isBalanced


heightBalancedBinaryTree(rootNode)