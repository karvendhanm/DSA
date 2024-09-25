class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# tree 1
tree1 = BinaryTree(1)
# left
tree1.left = BinaryTree(3)
tree1.left.left = BinaryTree(7)
tree1.left.right = BinaryTree(4)

# right
tree1.right = BinaryTree(2)

# tree 2
tree2 = BinaryTree(1)
# left
tree2.left = BinaryTree(5)
tree2.left.left = BinaryTree(2)

# right
tree2.right = BinaryTree(9)
tree2.right.left = BinaryTree(7)
tree2.right.right = BinaryTree(6)


def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    return None


mergeBinaryTrees(tree1, tree2)
