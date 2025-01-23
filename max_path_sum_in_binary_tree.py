class BT:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BT(-1)

# left branch
root.left = BT(-2)
root.left.left = BT(-4)
root.left.right = BT(-5)

# right branch
root.right = BT(-3)
root.right.right = BT(-7)
root.right.left = BT(-6)


# O(n) time | O(log(n)) space
def maxPathSum(tree):
    _, maxPathSum = maxPathSumHelper(tree)
    return maxPathSum


def maxPathSumHelper(tree):
    # Write your code here.
    if tree is None:
        return 0, float('-inf')

    leftMaxSumAsBranch, leftMaxPathSum = maxPathSumHelper(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = maxPathSumHelper(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNode = max(maxSumAsBranch, leftMaxSumAsBranch + value + rightMaxSumAsBranch)
    maxPathSum = max(maxSumAsRootNode, leftMaxPathSum, rightMaxPathSum)
    return maxSumAsBranch, maxPathSum


print(maxPathSum(root))
