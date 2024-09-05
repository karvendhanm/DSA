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


def validateBstHelper(tree, minValue=float('-inf'), maxValue=float('inf')):
    if tree is None:
        return True

    if tree.value < minValue or tree.value >= maxValue:
        return False

    left_flag, right_flag = True, True
    if tree.left is not None:
        left_flag = validateBstHelper(tree.left, minValue, tree.value)

    if tree.right is not None:
        right_flag = validateBstHelper(tree.right, tree.value, maxValue)

    return left_flag and right_flag


# O(n) time | O(d) space.
def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree)


validateBst(rootNode)
