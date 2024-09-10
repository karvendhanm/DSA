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


def findKthLargestValueInBst(tree, k):
    """

    :param tree:
    :param k:
    :return:
    """
    stack = []
    while True:
        if tree:
            stack.append(tree)
            tree = tree.right
            continue
        tree = stack.pop()
        k -= 1
        if k == 0:
            return tree.value
        tree = tree.left


print(findKthLargestValueInBst(rootNode, 5))
