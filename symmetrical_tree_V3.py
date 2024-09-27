class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# tree 1
tree = BinaryTree(1)
# left subtree
tree.left = BinaryTree(2)
tree.left.right = BinaryTree(4)
tree.left.left = BinaryTree(3)
tree.left.left.left = BinaryTree(5)
tree.left.left.right = BinaryTree(6)

# right subtree
tree.right = BinaryTree(2)
tree.right.left = BinaryTree(4)
tree.right.right = BinaryTree(3)
tree.right.right.right = BinaryTree(5)
tree.right.right.left = BinaryTree(6)


# O(n) time | o(h) space
# where n is the number of nodes in the tree
# where h is the height/depth of the tree
def symmetricalTreeHelper(leftSubTree, rightSubTree):
    if leftSubTree is not None and rightSubTree is not None and leftSubTree.value == rightSubTree.value:
        return (symmetricalTreeHelper(leftSubTree.left, rightSubTree.right) and
                symmetricalTreeHelper(leftSubTree.right, rightSubTree.left))

    return leftSubTree == rightSubTree


def symmetricalTree(tree):
    # Write your code here.
    return symmetricalTreeHelper(tree.left, tree.right)


symmetricalTree(tree)
