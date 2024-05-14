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


treeroot = BST(10).insert(5).insert(2).insert(5).insert(1).insert(15).insert(13).insert(22).insert(14)


def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, float('inf'))


# time complexity - Average: O(n log(n)), worst : O(n)
# space complexity - Average: O(n log(n)), worst: O(n) because of the frames used by the call stack
def findClosestValueInBSTHelper(tree, target, closest_value):

    if tree is None:
        return closest_value

    if abs(tree.value - target) < abs(closest_value - target):
        closest_value = tree.value

    if target < tree.value:
        return findClosestValueInBSTHelper(tree.left, target, closest_value)
    elif target > tree.value:
        return findClosestValueInBSTHelper(tree.right, target, closest_value))

    return closest_value


print(findClosestValueInBST(treeroot, 12))
