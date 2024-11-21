# O(n! * n^2) time | O(n! * n) space
def getPermutations(array):
    # Write your code here.
    permutations = []
    getPermutationsHelper(array, [], permutations)
    return permutations


def getPermutationsHelper(array, permutation, permutations):
    if not array and permutation:
        permutations.append(permutation)
        return
    else:
        for i in range(len(array)):
            newArr = array[:i] + array[i+1:]
            newPermutation = permutation + [array[i]]
            getPermutationsHelper(newArr, newPermutation, permutations)


array = [1, 2, 3]
print(getPermutations(array))
