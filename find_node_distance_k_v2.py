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


# O(n) time | O(n) space
def findNodesDistanceK(tree, target, k):
    # Write your code here.
    parents, nodeValuesAtK, visitedNodes = {}, [], set()

    assignParentNode(tree, None, parents)
    targetNode = getTargetNode(target, tree, parents)
    getNodesAtDistanceK(targetNode, parents, visitedNodes, 0, k, nodeValuesAtK)
    return nodeValuesAtK


def getNodesAtDistanceK(targetNode, parents, visitedNodes, distance, targetDistance, nodeValuesAtK):
    queue = [(targetNode, distance)]

    while queue:
        node, currentDistance = queue.pop(0)

        visitedNodes.add(node.value)

        if currentDistance == targetDistance:
            nodeValuesAtK.append(node.value)
            break

        value = node.value
        if node.left is not None and node.left.value not in visitedNodes:
            queue.append((node.left, currentDistance + 1))
        if node.right is not None and node.right.value not in visitedNodes:
            queue.append((node.right, currentDistance + 1))
        if parents[value] is not None and parents[value].value not in visitedNodes:
            queue.append((parents[value], currentDistance + 1))

    for elem in queue:
        nodeValuesAtK.append(elem[0].value)

    return


def getTargetNode(target, tree, parents):
    if parents[target] is None:
        return tree
    elif parents[target].left is not None and parents[target].left.value == target:
        return parents[target].left
    else:
        return parents[target].right


def assignParentNode(tree, parentNode, parents):
    if tree is None:
        return

    parents[tree.value] = parentNode
    assignParentNode(tree.left, tree, parents)
    assignParentNode(tree.right, tree, parents)

    return


print(findNodesDistanceK(tree, 3, 2))