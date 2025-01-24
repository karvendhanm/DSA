class BT:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent



tree = BT(1)

# left
tree.left = BT(2)
tree.left.left = BT(4)
tree.left.right = BT(5)

# right
tree.right = BT(3)
tree.right.right = BT(6)
tree.right.right.left = BT(7)
tree.right.right.right = BT(8)


def findNodesDistanceK(tree, target, k):
    # Write your code here.
    assignParentNode(tree, None)
    return


def assignParentNode(tree, parentNode):
    if tree is None:
        return
    assignParentNode(tree.left, tree)
    assignParentNode(tree.right, tree)
    tree.parent = parentNode
    return


print(findNodesDistanceK(tree=tree, target=3, k=2))