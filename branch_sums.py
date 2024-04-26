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

# time: O(n) and space O(n)
# space complexity is O(n) because of the
# frames we use in the call stack
def branchSums(root):
    # Write your code here.
    branchSums = []
    branchSumsHelper(root, 0, branchSums)
    return branchSums


def branchSumsHelper(root, runningSum, branchSums):
    if root is None:
        return

    runningSum += root.value

    if root.left is None and root.right is None:
        branchSums.append(runningSum)
        return

    branchSumsHelper(root.left, runningSum, branchSums)
    branchSumsHelper(root.right, runningSum, branchSums)


branchSums(tree_root)




