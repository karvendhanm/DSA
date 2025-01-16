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


# def isParentNode(parentNode, childNode):
#     if parentNode is None or childNode is None:
#         return False

#     if parentNode == childNode:
#         return True
#     return isParentNode(parentNode.left, childNode) or isParentNode(parentNode.right, childNode)


# # first iteration
# # O(n) time | O(n) space
# # where n is the number of nodes of the BST
# def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
#     # Write your code here.
#     if isParentNode(nodeOne, nodeTwo):
#         if isParentNode(nodeTwo, nodeThree):
#             return True
#     elif isParentNode(nodeThree, nodeTwo):
#         if isParentNode(nodeTwo, nodeOne):
#             return True
#     return False


# def isParentNode(parentNode, childNode):
#     if parentNode is None or childNode is None:
#         return False

#     while parentNode is not None:
#         if parentNode == childNode:
#             return True
#         elif childNode.value < parentNode.value:
#             parentNode = parentNode.left
#         elif childNode.value >= parentNode.value:
#             parentNode = parentNode.right
#     return False


def isParentNode(parentNode, childNode):
    while parentNode is not None and parentNode is not childNode:
        parentNode = parentNode.left if childNode.value < parentNode.value else parentNode.right
    return parentNode is childNode


# second iteration
# O(d) time | O(1) space
# where d is the maximum depth of the BST
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    if isParentNode(nodeOne, nodeTwo) and isParentNode(nodeTwo, nodeThree):
        return True
    elif isParentNode(nodeThree, nodeTwo) and isParentNode(nodeTwo, nodeOne):
        return True
    return False


print(validateThreeNodes(nodeOne, nodeTwo, nodeThree))
