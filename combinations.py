def getCombinations(n, r):
    combinations = []
    return getCombinationsHelper(0, n, r, combinations, [])


def getCombinationsHelper(i, n, r, combinations, combination):
    if len(combination) == r:
        combinations.append(combination)
        return

    for j in range(i, min(n, i + r + 1)):
        if any(num >= j for num in combination):
            continue
        newCombination = combination + [j]
        getCombinationsHelper(i + 1, n, r, combinations, newCombination)
    return combinations


getCombinations(5, 4)
