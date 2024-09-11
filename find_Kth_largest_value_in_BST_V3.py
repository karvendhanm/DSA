class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right

        return self


rootNode = BST(5).insert(4).insert(3).insert(6).insert(7).insert(6)


class TreeInfo(object):
    def __init__(self, latestVisitedNodeValue, numberOfNodesVisited):
        self.latestVisitedNodeValue = latestVisitedNodeValue
        self.numberOfNodesVisited = numberOfNodesVisited


# O(h + k) time | O(h) space.
# where h is the height or maximum depth of the tree,
# and k is the number of nodes visited
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(-1, 0)
    findKthLargestValueInBstHelper(tree, k, treeInfo)
    return treeInfo.latestVisitedNodeValue


def findKthLargestValueInBstHelper(tree, k, treeInfo):
    if tree is None or treeInfo.numberOfNodesVisited >= k:
        return

    findKthLargestValueInBstHelper(tree.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.latestVisitedNodeValue = tree.value
        treeInfo.numberOfNodesVisited += 1
        findKthLargestValueInBstHelper(tree.left, k, treeInfo)


print(findKthLargestValueInBst(rootNode, 5))
