# first iteration
# O(n^2) time | O(1) time
# sub-optimal time complexity
# def subarraySort(array):
#     # Write your code here.
#     # identifying smaller numbers going from the left:
#     indices = [-1, -1]
#     leftIndexFound = rightIndexFound = False
#     for idx in range(len(array)):
#         left = idx + 1
#         while left < len(array):
#             if array[left] < array[idx]:
#                 indices[0] = idx
#                 leftIndexFound = True
#                 break
#             left += 1
#         if leftIndexFound:
#             break
#     for idx in range(len(array)-1, -1, -1):
#         right = idx - 1
#         while right >= 0:
#             if array[right] > array[idx]:
#                 indices[1] = idx
#                 rightIndexFound = True
#                 break
#             right -= 1
#         if rightIndexFound:
#             break
#     return indices


# second iteration
# O(n) time | O(1) time
# def subarraySort(array):
#     smallestUnsortedNumber = float('inf')
#     largestUnsortedNumber = float('-inf')
#     # finding all the unsorted numbers in the array
#     for idx in range(len(array)):
#         if (idx - 1 >= 0 and array[idx] < array[idx - 1]) or (idx + 1 < len(array) and array[idx] > array[idx + 1]):
#             smallestUnsortedNumber = min(array[idx], smallestUnsortedNumber)
#             largestUnsortedNumber = max(array[idx], largestUnsortedNumber)
#
#     indices = [-1, -1]
#     if smallestUnsortedNumber == float('inf'):
#         return indices
#
#     for i in range(len(array)):
#         if array[i] > smallestUnsortedNumber:
#             indices[0] = i
#             break
#
#     for i in reversed(range(len(array))):
#         if array[i] < largestUnsortedNumber:
#             indices[1] = i
#             break
#     return indices


# third iteration
# O(n) time | O(1) time
def subarraySort(array):
    smallestUnsortedNumber = float('inf')
    largestUnsortedNumber = float('-inf')

    for i in range(len(array)):
        if isUnsortedNumber(i, array):
            smallestUnsortedNumber = min(array[i], smallestUnsortedNumber)
            largestUnsortedNumber = max(array[i], largestUnsortedNumber)

    if smallestUnsortedNumber == float('inf'):
        return [-1, -1]

    leftIndex = 0
    rightIndex = len(array) - 1
    while array[leftIndex] <= smallestUnsortedNumber:
        leftIndex += 1
    while array[rightIndex] >= largestUnsortedNumber:
        rightIndex -= 1
    return [leftIndex, rightIndex]


def isUnsortedNumber(idx, array):
    # this logic works as we have been assured
    # that at least there will be 2 numbers in the incoming array
    if idx == 0:
        return array[idx + 1] < array[idx]
    if idx == len(array)-1:
        return array[idx] < array[idx-1]
    return array[idx - 1] > array[idx] or array[idx] > array[idx + 1]


array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(array))
