# O(n log n) time | O(1) space
def largestRange(array):
    # Write your code here.
    array.sort()
    currentRangeStartIdx = 0
    maxRangeStartIdx = maxRangeEndIdx = 0
    for i in range(len(array)):
        if isEndOfARange(i, array):
            currentMaxRange = maxRangeEndIdx - maxRangeStartIdx
            if (array[currentRangeStartIdx] != array[i]) and ((i - currentRangeStartIdx) > currentMaxRange):
                maxRangeEndIdx = i
                maxRangeStartIdx = currentRangeStartIdx
            currentRangeStartIdx = i + 1
    return [array[maxRangeStartIdx], array[maxRangeEndIdx]]


def isEndOfARange(i, array):
    if i == len(array) - 1:
        return True
    return array[i + 1] - array[i] >= 2


array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array))