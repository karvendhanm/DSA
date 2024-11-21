# first iteration
# O(n! * n^2) time | O(n! * n) space
# def getPermutations(array):
#     # Write your code here.
#     permutations = []
#     getPermutationsHelper(array, [], permutations)
#     return permutations
#
#
# def getPermutationsHelper(array, permutation, permutations):
#     if not array and permutation:
#         permutations.append(permutation)
#         return
#     else:
#         for i in range(len(array)):
#             newArr = array[:i] + array[i+1:]
#             newPermutation = permutation + [array[i]]
#             getPermutationsHelper(newArr, newPermutation, permutations)


# second iteration
# O(n! * n) time | O(n! * n) space
def getPermutations(array):
    # Write your code here.
    permutations = []
    getPermutationsHelper(0, array, permutations)
    return permutations


def getPermutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            array[i], array[j] = array[j], array[i]
            getPermutationsHelper(i+1, array, permutations)
            array[i], array[j] = array[j], array[i]


array = [1, 2, 3]
print(getPermutations(array))


