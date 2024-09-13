# This is the class of the input binary tree.
class BT:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = BT(1)
tree.left = BT(2)
tree.left.left = BT(4)
tree.left.right = BT(5)
tree.left.left.left = BT(8)
tree.left.left.rigth = BT(8)
tree.right = BT(3)
tree.right.left = BT(6)
tree.right.right = BT(7)


# second iteration iterative solution
# O(n) time | O(n) space
# at any given time
def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return

    stack = [tree]

    while stack:
        currentNode = stack.pop(0)

        if currentNode is not None:
            currentNode.left, currentNode.right = currentNode.right, currentNode.left

            stack.append(currentNode.left)
            stack.append(currentNode.right)

    return tree


print(invertBinaryTree(tree))