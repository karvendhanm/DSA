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


# first iteration
def mergeBinaryTreeshelper(tree1, tree2):
    if tree1 is None and tree2 is None:
        return None

    if tree1.left is None and tree2.left is not None:
        tree1.left = BinaryTree(0)
    elif tree1.left is not None and tree2.left is None:
        tree2.left = BinaryTree(0)

    if tree1.right is None and tree2.right is not None:
        tree1.right = BinaryTree(0)
    elif tree1.right is not None and tree2.right is None:
        tree2.right = BinaryTree(0)

    tree1.left = mergeBinaryTreeshelper(tree1.left, tree2.left)
    tree1.right = mergeBinaryTreeshelper(tree1.right, tree2.right)

    tree1.value += tree2.value

    return tree1


def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    return mergeBinaryTreeshelper(tree1, tree2)


mergeBinaryTrees(tree1, tree2)
