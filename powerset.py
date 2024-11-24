# O(n * 2^n) time | O(n * 2^n) space
# def powerset(array):
#     powerset = []
#     powersetHelper(array, [], powerset)
#     return powerset
#
#
# def powersetHelper(array, currentPowerset, powerset):
#     powerset.append(currentPowerset)
#     for i in range(len(array)):
#         newArr = array[i + 1:]
#         newPowerset = currentPowerset + [array[i]]
#         powersetHelper(newArr, newPowerset, powerset)


# O(n * 2^n) time | O(n * 2^n) space
# def powerset(array):
#     # iterative solution
#     subsets = [[]]
#     for elem in array:
#         for i in range(len(subsets)):
#             subsets.append(subsets[i] + [elem])
#     return subsets


# O(n * 2^n) time | O(n * 2^n) space
# Another recursive solution
# this recursive solution is based on the idea that
# P([1, 2]) = P([1]) + [2] added to all the subsets.
def powerset(array, idx=None):
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx-1)
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [ele])
    return subsets


array = [1, 2, 3]
print(powerset(array))
