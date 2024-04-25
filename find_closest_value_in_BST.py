# find closest value in binary search tree
# refer https://www.algoexpert.io/questions/find-closest-value-in-bst
# for the question to this solution.
def findClosestValueInBst(tree, target):
    # Write your code here.
    closest_value = float('inf')
    while tree is not None:
        if abs(target - tree.value) < abs(target - closest_value):
            closest_value = tree.value

        if tree.value == target:
            return target
        elif target > tree.value:
            tree = tree.right
        elif target < tree.value:
            tree = tree.left
    return closest_value
