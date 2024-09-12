class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# rootNode = BST(10).insert(4).insert(2).insert(1).insert(5).insert(17).insert(19).insert(18)


# second iteration
# O(n) time | O(n) space
# O(n) space as we are creating n BST objects.
def reconstructBst(preOrderTraversalValues):
    rootNode = BST(preOrderTraversalValues[0])

    left_values = []
    right_values = []

    for elem in preOrderTraversalValues[1:]:
        if elem < rootNode.value:
            left_values.append(elem)
        else:
            right_values.append(elem)

    if left_values:
        rootNode.left = reconstructBst(left_values)
    if right_values:
        rootNode.right = reconstructBst(right_values)

    return rootNode


preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
print(reconstructBst(preOrderTraversalValues))
