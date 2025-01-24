class BT:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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
    parentNodeDetails = {}
    assignParentNode(tree, None, parentNodeDetails)
    targetNode = identifyTargetNode(tree, target)
    return


def assignParentNode(tree, parentNode, parentNodeDetails):
    if tree is None:
        return
    assignParentNode(tree.left, tree, parentNodeDetails)
    assignParentNode(tree.right, tree, parentNodeDetails)
    parentNodeDetails[tree] = parentNode
    return


def identifyTargetNode(tree, target):
    if tree is None:
        return

    if tree.value == target:
        return tree

    left = identifyTargetNode(tree.left, target)
    if not left:
        right = identifyTargetNode(tree.right, target)

    return left or right





print(findNodesDistanceK(tree=tree, target=3, k=2))