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
rootNode.right.right.right = BinaryTree(10)


def getTreeHeight(node):
    if node is None:
        return 0

    leftHeight = getTreeHeight(node.left)
    rightHeight = getTreeHeight(node.right)

    return max(leftHeight, rightHeight) + 1


class BalancedBinaryTree(object):
    def __init__(self, flag):
        self.flag = flag

def heightBalancedBinaryTreeHelper(tree, obj):
    if tree is None or not obj.flag:
        return 0

    _left = heightBalancedBinaryTreeHelper(tree.left, obj)
    _right = heightBalancedBinaryTreeHelper(tree.right, obj)

    if abs(_left - _right) > 1 and obj.flag:
        obj.flag = False

    return getTreeHeight(tree)


# first iteration
def heightBalancedBinaryTree(tree):
    # Write your code here.
    obj = BalancedBinaryTree(True)
    heightBalancedBinaryTreeHelper(tree, obj)
    return obj.flag


print(heightBalancedBinaryTree(rootNode))
