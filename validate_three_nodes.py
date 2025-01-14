class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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


root = BST(5).insert(2).insert(1).insert(0).insert(4).insert(3).insert(7).insert(6).insert(8)
nodeOne = root
nodeTwo = root.left
nodeThree = root.left.right.left


def isParentNode(parentNode, childNode):
    if parentNode is None or childNode is None:
        return False

    if parentNode == childNode:
        return True
    return isParentNode(parentNode.left, childNode) or isParentNode(parentNode.right, childNode)


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    if isParentNode(nodeOne, nodeTwo):
        if isParentNode(nodeTwo, nodeThree):
            return True
    elif isParentNode(nodeThree, nodeTwo):
        if isParentNode(nodeTwo, nodeOne):
            return True
    return False


print(validateThreeNodes(nodeOne, nodeTwo, nodeThree))
