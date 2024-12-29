# first iteration
# O(n log n) time | O(1) space
# def largestRange(array):
#     # Write your code here.
#     currentRangeStartIdx = 0
#     maxRangeStartIdx = maxRangeEndIdx = 0
#     for i in range(len(array)):
#         if isEndOfARange(i, array):
#             currentMaxRange = maxRangeEndIdx - maxRangeStartIdx
#             if (array[currentRangeStartIdx] != array[i]) and ((i - currentRangeStartIdx) > currentMaxRange):
#                 maxRangeEndIdx = i
#                 maxRangeStartIdx = currentRangeStartIdx
#             currentRangeStartIdx = i + 1
#     return [array[maxRangeStartIdx], array[maxRangeEndIdx]]
#
#
# def isEndOfARange(i, array):
#     if i == len(array) - 1:
#         return True
#     return array[i + 1] - array[i] >= 2


# second iteration
# O(n) time | O(n) space
def largestRange(array):
    bestRange = []
    maxRangeLength = 0
    nums = {}

    for num in array:
        nums[num] = True

    for num in array:
        if not nums[num]:
            continue

        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1

        if currentLength > maxRangeLength:
            maxRangeLength = currentLength
            bestRange = [left+1, right-1]
    return bestRange


array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array))















