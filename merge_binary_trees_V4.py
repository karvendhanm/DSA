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



# O(n) time | O(h) space
# where n is the number of nodes of the smaller tree
# where h is the depth/height of the smaller tree
# sixth iteration
def mergeBinaryTrees(tree1, tree2):
    # iterative solution
    # if either of the tree is absent, return the other
    if tree1 is None or tree2 is None:
        return tree1 or tree2

    tree1Stack = [tree1]
    tree2Stack = [tree2]

    while len(tree1Stack) > 0:
        # tree1Node can't be None at this point
        tree1Node = tree1Stack.pop()
        tree2Node = tree2Stack.pop()

        # tree2Node can be None.
        if tree2Node is None:
            continue

        tree1Node.value += tree2Node.value

        if tree1Node.left is None:
            tree1Node.left = tree2Node.left
        else:
            tree1Stack.append(tree1Node.left)
            tree2Stack.append(tree2Node.left)

        if tree1Node.right is None:
            tree1Node.right = tree2Node.right
        else:
            tree1Stack.append(tree1Node.right)
            tree2Stack.append(tree2Node.right)

    return tree1


obj = mergeBinaryTrees(tree1, tree2)
