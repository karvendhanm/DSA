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
def powerset(array):
    # iterative solution
    subsets = [[]]
    for elem in array:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [elem])
    return subsets


array = [1, 2, 3]
print(powerset(array))
