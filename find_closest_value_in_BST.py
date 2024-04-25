# find closest value in binary search tree
# refer https://www.algoexpert.io/questions/find-closest-value-in-bst
# for the question to this solution.

# time complexity O(log n), space complexity O(1)
def findClosestValueInBst(tree, target):
    # Write your code here.

    closest_value = float('inf')
    while tree is not None:
        if abs(target - tree.value) < abs(target - closest_value):
            closest_value = tree.value

        if target > tree.value:
            tree = tree.right
        elif target < tree.value:
            tree = tree.left
        else:
            break
    return closest_value


# using a helper function - second iteration
# time complexity O(log n), space complexity O(1)
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))


def findClosestValueInBstHelper(tree, target, closest_value):
    while tree is not None:
        if abs(target - tree.value) < abs(target - closest_value):
            closest_value = tree.value

        if target > tree.value:
            tree = tree.right
        elif target < tree.value:
            tree = tree.left
        else:
            break
    return closest_value

# using a recursive function - third iteration
# time complexity O(log n), space complexity O(log n)
# here space complexity is also O(log n) because of the frames
# we use in the call stack.
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree, target, float('inf'))


def findClosestValueInBstHelper(tree, target, closest_value):
    # writing a recursive function
    if tree is None:
        return closest_value

    if abs(target - tree.value) < abs(target - closest_value):
        closest_value = tree.value

    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest_value)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest_value)
    else:
        return closest_value
