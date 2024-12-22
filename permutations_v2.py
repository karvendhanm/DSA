# def getPermutations(array):
#     # Write your code here.
#     permutations = []
#     return getPermutationsHelper(array, [], permutations)
#
#
# def getPermutationsHelper(array, permutation, permutations):
#     if not array and permutation:
#         permutations.append(permutation)
#         return
#
#     for i in range(len(array)):
#         newarray = array[:i] + array[i+1:]
#         newPermutation = permutation + [array[i]]
#         getPermutationsHelper(newarray, newPermutation, permutations)
#     return permutations


# swapping
def getPermutations(array):
    # Write your code here.
    permutations = []
    return getPermutationsHelper(0, array, permutations)


def getPermutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
        return

    for j in range(i, len(array)):
        array[i], array[j] = array[j], array[i]
        getPermutationsHelper(i+1, array, permutations)
        array[i], array[j] = array[j], array[i]
    return permutations


array = [1, 2, 3]
print(getPermutations(array))