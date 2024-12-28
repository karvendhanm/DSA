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
def subarraySort(array):
    smallestUnsortedNumber = float('inf')
    largestUnsortedNumber = float('-inf')
    # finding all the unsorted numbers in the array
    for idx in range(len(array)):
        if (idx - 1 >= 0 and array[idx] < array[idx - 1]) or (idx + 1 < len(array) and array[idx] > array[idx + 1]):
            smallestUnsortedNumber = min(array[idx], smallestUnsortedNumber)
            largestUnsortedNumber = max(array[idx], largestUnsortedNumber)

    indices = [-1, -1]
    if smallestUnsortedNumber == float('inf'):
        return indices

    for i in range(len(array)):
        if array[i] > smallestUnsortedNumber:
            indices[0] = i
            break

    for i in reversed(range(len(array))):
        if array[i] < largestUnsortedNumber:
            indices[1] = i
            break
    return indices


array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(array))
