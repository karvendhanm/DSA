class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


rootNode = BinaryTree(1)
# left
rootNode.left = BinaryTree(2, parent=rootNode)
rootNode.left.left = BinaryTree(4, parent=rootNode.left)
rootNode.left.left.left = BinaryTree(6, parent=rootNode.left.left)
rootNode.left.right = BinaryTree(5, parent=rootNode.left)

# right
rootNode.right = BinaryTree(3, parent=rootNode)


# O(n) time | O(n) space
# both time and space complexity are not optimal.
def findSuccessor(tree, node):
    # Write your code here.
    _lst = []
    findSuccessorHelper(tree, node, _lst)
    _idx = _lst.index(node)
    if _idx + 1 < len(_lst):
        return _lst[_idx + 1]
    else:
        return None


def findSuccessorHelper(tree, node, _lst):

    if tree is None:
        return None

    findSuccessorHelper(tree.left, node, _lst)
    _lst.append(tree)
    findSuccessorHelper(tree.right, node, _lst)

    return _lst


print(findSuccessor(rootNode, 5))
