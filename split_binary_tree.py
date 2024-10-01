class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# tree 1
# tree = BinaryTree(1)
# # left subtree
# tree.left = BinaryTree(3)
# tree.left.right = BinaryTree(-5)
# tree.left.left = BinaryTree(6)
# tree.left.left.left = BinaryTree(2)
#
# # right subtree
# tree.right = BinaryTree(-2)
# tree.right.left = BinaryTree(5)
# tree.right.right = BinaryTree(2)


# tree 1
tree = BinaryTree(1)
# left subtree
tree.left = BinaryTree(1)
tree.left.left = BinaryTree(12)
tree.left.left.right = BinaryTree(-21)

# right subtree
tree.right = BinaryTree(2)
tree.right.right = BinaryTree(-5)


def splitBinaryTreeHelper(tree, _lst):
    if tree is None:
        return 0

    _left = splitBinaryTreeHelper(tree.left, _lst)
    _right = splitBinaryTreeHelper(tree.right, _lst)

    tot_val = _left + _right + tree.value
    _lst.append(tot_val)

    return tot_val


# first iteration
# O(n) time | O(n) space
def splitBinaryTree(tree):
    # Write your code here.
    _lst = []
    splitBinaryTreeHelper(tree, _lst)
    max_elem = _lst[-1]
    remain_element = set(_lst[:-1])
    for elem in remain_element:
        if 2 * elem == max_elem:
            return elem
    return 0


splitBinaryTree(tree)