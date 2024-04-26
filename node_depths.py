# create BST object

class BST(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right
        return self


tree_root = BST(12).insert(9).insert(6).insert(3).insert(7).insert(8).insert(10).insert(11).insert(15).insert(16)

def nodeDepths(root):
    # Write your code here.
    return nodeDepthsHelper(root, 0, 0)


def nodeDepthsHelper(root, nodeLevel, nodeDepth):
    if root is None:
        return nodeDepth

    nodeDepth += nodeLevel

    if root.left is None and root.right is None:
        return nodeDepth

    nodeDepth = nodeDepthsHelper(root.left, nodeLevel+1, nodeDepth)
    nodeDepth = nodeDepthsHelper(root.right, nodeLevel+1, nodeDepth)

    return nodeDepth


print(nodeDepths(tree_root))