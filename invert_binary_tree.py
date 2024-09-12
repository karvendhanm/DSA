# This is the class of the input binary tree.
class BT:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = BT(1)
tree.left = BT(2)
tree.left.left = BT(4)
tree.left.right = BT(5)
tree.left.left.left = BT(8)
tree.left.left.rigth = BT(8)
tree.right = BT(3)
tree.right.left = BT(6)
tree.right.right = BT(7)


# O(n) time | O(d) space
def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return

    tree.left, tree.right = tree.right, tree.left

    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

    return tree


invertBinaryTree(tree)