# first iteration
# O(n) time | O(n) space
# def maxSubsetSumNoAdjacent(array):
#     # Write your code here.
#     if not len(array):
#         return 0
#     if len(array) == 1:
#         return array[0]
#     maxSums = array[:]
#     maxSums[1] = max(array[0], array[1])
#
#     for i in range(2, len(maxSums)):
#         maxSums[i] = max(maxSums[i-1], maxSums[i-2]+array[i])
#     return maxSums[-1]


# second iteration
# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not len(array):
        return 0
    if len(array) == 1:
        return array[0]
    first = array[0]
    second = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(second, first + array[i])
        first = second
        second = current
    return second


array = [4, 3, 5, 200, 5, 3]
print(maxSubsetSumNoAdjacent(array))
