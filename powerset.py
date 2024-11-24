# O(n * 2^n) time | O(n * 2^n) space
def powerset(array):
    pow = []
    powersetHelper(array, [], pow)
    return pow


def powersetHelper(array, currentPermutation, permutations):
    permutations.append(currentPermutation)
    for i in range(len(array)):
        newArr = array[i + 1:]
        newPermutation = currentPermutation + [array[i]]
        powersetHelper(newArr, newPermutation, permutations)


array = [1, 2, 3]
print(powerset(array))
