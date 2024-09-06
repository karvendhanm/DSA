class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
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


def inOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return

    inOrderTraverse(tree.left, array)
    array.append(tree.value)

    inOrderTraverse(tree.right, array)

    return array


def preOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return

    array.append(tree.value)

    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)

    return array


def postOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return

    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)

    return array


rootNode = BST(10).insert(5).insert(2).insert(1).insert(5).insert(15).insert(13).insert(22).insert(14).insert(12)
print(postOrderTraverse(rootNode, []))
