class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# tree 1
tree = BinaryTree(1)
# left subtree
tree.left = BinaryTree(3)
tree.left.right = BinaryTree(-5)
tree.left.left = BinaryTree(6)
tree.left.left.left = BinaryTree(2)

# right subtree
tree.right = BinaryTree(-2)
tree.right.left = BinaryTree(5)
tree.right.right = BinaryTree(2)


def splitBinaryTreeHelper(tree, desired_sum):
    if tree is None:
        return 0, False

    _left, leftCanBeSplit = splitBinaryTreeHelper(tree.left, desired_sum)
    _right, rightCanBeSplit = splitBinaryTreeHelper(tree.right, desired_sum)

    tot_val = _left + _right + tree.value
    canBeSplit = leftCanBeSplit or rightCanBeSplit or tot_val == desired_sum
    return tot_val, canBeSplit


# O(n) time | O(1) space
def getTreeSum(tree):
    if tree is None:
        return 0

    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)


# second iteration
# O(n) time | O(h) space
# h is the height of the tree
def splitBinaryTree(tree):
    # Write your code here.
    desired_sum = getTreeSum(tree) / 2
    canBeSplit = splitBinaryTreeHelper(tree, desired_sum)[1]
    return desired_sum if canBeSplit else 0


splitBinaryTree(tree)