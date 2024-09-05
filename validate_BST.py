# This is an input class. Do not edit.
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


rootNode = BST(10).insert(5).insert(2).insert(1).insert(5).insert(15).insert(22).insert(13).insert(14)

def validateBstHelper(tree, minValue, maxValue):

    if tree is None:
        return True

def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree)
