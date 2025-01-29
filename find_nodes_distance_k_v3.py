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


def getNodesAtDistanceK(tree, currentDistance, targetDistance, nodesAtDistanceK):
    if tree is None or currentDistance > targetDistance:
        return

    if currentDistance == targetDistance:
        nodesAtDistanceK.append(tree.value)
        return

    getNodesAtDistanceK(tree.left, currentDistance + 1, targetDistance, nodesAtDistanceK)
    getNodesAtDistanceK(tree.right, currentDistance + 1, targetDistance, nodesAtDistanceK)

    return


def findNodesDistanceKHelper(tree, target, k, nodesAtDistanceK, currentDistance):
    if tree is None:
        return -1

    if tree.value == target:
        getNodesAtDistanceK(tree, 0, k, nodesAtDistanceK)
        return currentDistance

    left = findNodesDistanceKHelper(tree.left, target, k, nodesAtDistanceK, currentDistance + 1)
    right = findNodesDistanceKHelper(tree.right, target, k, nodesAtDistanceK, currentDistance + 1)

    if left != -1:
        targetDistance = k - (left - currentDistance)
        if targetDistance == 0:
            nodesAtDistanceK.append(tree.value)
        elif targetDistance > 0:
            getNodesAtDistanceK(tree.right, 1, targetDistance, nodesAtDistanceK)
        return left
    elif right != -1:
        targetDistance = k - (right - currentDistance)
        if targetDistance == 0:
            nodesAtDistanceK.append(tree.value)
        elif targetDistance > 0:
            getNodesAtDistanceK(tree.left, 1, targetDistance, nodesAtDistanceK)
        return right
    return -1


# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    nodesAtDistanceK = []
    findNodesDistanceKHelper(tree, target, k, nodesAtDistanceK, 0)
    return nodesAtDistanceK


print(findNodesDistanceK(tree, 3, 2))
