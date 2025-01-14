# second iteration
# O(n^2) time | O(d) space
# worst case O(n^2) time | O(n) space
# where d is the depth of the BST
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    return sameBstsHelper(arrayOne, arrayTwo, 0, 0, float('-inf'), float('inf'))


def sameBstsHelper(arrayOne, arrayTwo, rootIdxArrayOne, rootIdxArrayTwo, minVal, maxVal):
    if rootIdxArrayOne == -1 or rootIdxArrayTwo == -1:
        return rootIdxArrayOne == rootIdxArrayTwo

    if arrayOne[rootIdxArrayOne] != arrayTwo[rootIdxArrayTwo]:
        return False

    currentValue = arrayOne[rootIdxArrayOne]
    leftBSTRootIdxArrayOne = getSmallerValIdxFromRootIdx(arrayOne, rootIdxArrayOne, minVal, maxVal)
    leftBSTRootIdxArrayTwo = getSmallerValIdxFromRootIdx(arrayTwo, rootIdxArrayTwo, minVal, maxVal)
    rightBSTRootIdxArrayOne = getBiggerOrEqualValIdxFromRootIdx(arrayOne, rootIdxArrayOne, minVal, maxVal)
    rightBSTRootIdxArrayTwo = getBiggerOrEqualValIdxFromRootIdx(arrayTwo, rootIdxArrayTwo, minVal, maxVal)

    leftBSTsSame = sameBstsHelper(arrayOne, arrayTwo, leftBSTRootIdxArrayOne, leftBSTRootIdxArrayTwo, minVal, currentValue)
    rightBSTsSame = sameBstsHelper(arrayOne, arrayTwo, rightBSTRootIdxArrayOne, rightBSTRootIdxArrayTwo, currentValue, maxVal)

    return leftBSTsSame and rightBSTsSame


def getSmallerValIdxFromRootIdx(array, rootIdx, minVal, maxVal):
    for i in range(rootIdx + 1, len(array)):
        if array[i] < array[rootIdx] and array[i] >= minVal:
            return i
    return -1


def getBiggerOrEqualValIdxFromRootIdx(array, rootIdx, minVal, maxVal):
    for i in range(rootIdx + 1, len(array)):
        if array[i] >= array[rootIdx] and array[i] < maxVal:
            return i
    return -1


arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
print(sameBsts(arrayOne, arrayTwo))

