class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


tree = BinaryTree(1)

#left
tree.left = BinaryTree(3)
tree.left.left = BinaryTree(7)
tree.left.left.left = BinaryTree(8)
tree.left.left.left.left = BinaryTree(9)

# left - right
tree.left.right = BinaryTree(4)
tree.left.right.right = BinaryTree(5)
tree.left.right.right.right = BinaryTree(6)

# right
tree.right = BinaryTree(2)


# first iteration
# O(n) time | O(h) space
# n - number of nodes in the tree
# h - height of the tree 
def binaryTreeDiameter(tree):
    # Write your code here.
    _lst = [float('-inf')]
    binaryTreeDiameterHelper(tree, _lst)
    return _lst[0]


def binaryTreeDiameterHelper(tree, _lst):
    if tree is None:
        return 0

    _left = binaryTreeDiameterHelper(tree.left, _lst)
    _right = binaryTreeDiameterHelper(tree.right, _lst)

    if _left + _right > _lst[0]:
        _lst[0] = _left + _right

    return max(_left, _right) + 1


print(binaryTreeDiameter(tree))
