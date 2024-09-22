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


class GetSuccessor(object):
    def __init__(self, target_node):
        self.target_node = target_node
        self.flag = 0
        self.successor_node = None

    def get_successor_node(self, tree):
        if tree is not None and self.flag == 1:
            self.flag = 0
            self.successor_node = tree

    def is_target_node(self, tree):
        if self.flag == 0 and self.target_node == tree:
            self.flag = 1


# second iteration
# O(h + k) time | O(h) space
# h - height or maximum depth of the tree
# k - number of nodes visited
def findSuccessor(tree, node):
    # Write your code here.
    successor = GetSuccessor(node)
    return findSuccessorHelper(tree, node, successor)


def findSuccessorHelper(tree, node, successor):

    if tree is None or successor.successor_node is not None:
        return successor.successor_node

    findSuccessorHelper(tree.left, node, successor)
    successor.get_successor_node(tree)
    successor.is_target_node(tree)
    findSuccessorHelper(tree.right, node, successor)

    return successor.successor_node


print(findSuccessor(rootNode, rootNode.left.right))
