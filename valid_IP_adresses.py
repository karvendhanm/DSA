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


def getValidIPAddresses(arrays):
    validStrings = []
    for array in arrays:
        splitStrings = array.split('.')
        for idx, string in enumerate(splitStrings):
            if (int(string) > 255 or len(string) > 3
                    or (int(string) == 0 and len(string) > 1)
                    or (int(string) > 0 and string[0] == '0')):
                break
            if idx >= 3:
                validStrings.append(array)
    return validStrings


# first iteration
def validIPAddresses(string):
    # Write your code here.
    allIPAddress = []
    strLength = len(string)
    allCombinations = getCombinations(list(range(strLength - 1)), 3)
    for combination in allCombinations:
        IPAddress = []
        for idx, char in enumerate(string):
            IPAddress.append(char)
            if idx in combination:
                IPAddress.append('.')
        allIPAddress.append("".join(IPAddress))
    return getValidIPAddresses(allIPAddress)


string = '1921680'
print(validIPAddresses(string))
