# O(nCr * (r * n)) time | O(nCr * r) space
# where n is the length of the array
def getCombinations(array, r):
    combinations = []
    return getCombinationsHelper(array, r, [], combinations)


def getCombinationsHelper(array, r, combination, combinations):
    if len(combination) == r:
        combinations.append(combination)
        return

    for idx, elem in enumerate(array):
        if idx > r:
            return combinations

        newCombination = combination + [elem]
        getCombinationsHelper(array[idx+1:], r, newCombination, combinations)
    return combinations


array = []
print(getCombinations(array, 3))
