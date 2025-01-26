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


# first iteration
# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    # Write your code here.
    parentNodeDetails, nodeValuesAtK, targetNode = {}, [], []

    # O(n) time | O(n) space
    assignParentNode(tree, None, parentNodeDetails, target, targetNode)
    # targetNode = identifyTargetNode(tree, target)
    # O(k) time | O(k) space
    getNodeAtKDistance(targetNode[0], 0, k, nodeValuesAtK, parentNodeDetails, {})
    return nodeValuesAtK


# O(k) time | O(k) space
def getNodeAtKDistance(node, currentDistance, targetDistance,
                       nodeValuesAtK, parentNodeDetails, visitedNodeTracker):
    if (node is None
            or currentDistance > targetDistance
            or node in visitedNodeTracker):
        return

    visitedNodeTracker[node] = True

    if currentDistance == targetDistance:
        nodeValuesAtK.append(node.value)
        return

    getNodeAtKDistance(parentNodeDetails[node], currentDistance + 1, targetDistance,
                       nodeValuesAtK, parentNodeDetails, visitedNodeTracker)
    getNodeAtKDistance(node.left, currentDistance + 1, targetDistance,
                       nodeValuesAtK, parentNodeDetails, visitedNodeTracker)
    getNodeAtKDistance(node.right, currentDistance + 1, targetDistance,
                       nodeValuesAtK, parentNodeDetails, visitedNodeTracker)

    return


# O(n) time | O(n) space
# where n is the number of nodes in the binary tree.
# space is O(n) because of parentNodeDetails dictionary.
def assignParentNode(tree, parentNode, parentNodeDetails, target, targetNode):
    if tree is None:
        return

    if tree.value == target:
        targetNode.append(tree)

    assignParentNode(tree.left, tree, parentNodeDetails, target, targetNode)
    assignParentNode(tree.right, tree, parentNodeDetails, target, targetNode)
    parentNodeDetails[tree] = parentNode
    return


# def identifyTargetNode(tree, target):
#     if tree is None:
#         return None
#
#     if tree.value == target:
#         return tree
#
#     left, right = None, None
#     left = identifyTargetNode(tree.left, target)
#     if not left:
#         right = identifyTargetNode(tree.right, target)
#
#     return left or right


print(findNodesDistanceK(tree=tree, target=3, k=2))