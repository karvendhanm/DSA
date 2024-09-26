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


# third iteration
# def mergeBinaryTrees(tree1, tree2):
#     if tree1 is None and tree2 is None:
#         return None
#
#     tree1 = tree1 or BinaryTree(0)
#     tree2 = tree2 or BinaryTree(0)
#
#     tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
#     tree1.right = mergeBinaryTrees(tree1.right, tree2.right)
#
#     tree1.value += tree2.value
#
#     return tree1


# fourth iteration
def mergeBinaryTrees(tree1, tree2):
    if tree1 is None and tree2 is None:
        return None

    tree1 = tree1 or BinaryTree(0)
    tree2 = tree2 or BinaryTree(0)

    newTree = BinaryTree(tree1.value + tree2.value)

    newTree.left = mergeBinaryTrees(tree1.left, tree2.left)
    newTree.right = mergeBinaryTrees(tree1.right, tree2.right)

    return newTree


# fifth iteration
# O(n) time and O(h) space
# where n is the number of nodes of the smaller tree
# where h is the depth/height of the smaller tree
def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    if tree1 is None or tree2 is None:
        return tree1 or tree2

    tree1.value += tree2.value

    tree1.left = mergeBinaryTrees(tree1.left, tree2.left)
    tree1.right = mergeBinaryTrees(tree1.right, tree2.right)

    return tree1


obj = mergeBinaryTrees(tree1, tree2)
