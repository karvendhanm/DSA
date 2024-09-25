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


# second iteration
def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if tree1 and tree2:
        newTree = BinaryTree(tree1.value + tree2.value)
        newTree.left = mergeBinaryTrees(tree1.left, tree2.left)
        newTree.right = mergeBinaryTrees(tree1.right, tree2.right)
        return newTree

    return tree1 or tree2


obj = mergeBinaryTrees(tree1, tree2)