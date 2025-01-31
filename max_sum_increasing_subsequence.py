# # first iteration
# # O(n^2) time | O(n) space
# def maxSumIncreasingSubsequence(array):
#     # Write your code here.
#     arrLength = len(array)
#     sums = array.copy()
#     sequences = [None for _ in range(arrLength)]
#     for i in range(arrLength):
#         for j in range(0, i):
#             if array[j] < array[i] and array[i] + sums[j] > sums[i]:
#                 sums[i] = array[i] + sums[j]
#                 sequences[i] = j
#     biggestSumIndex = 0
#     for idx, sum in enumerate(sums):
#         if sum > sums[biggestSumIndex]:
#             biggestSumIndex = idx
#     biggestSum = sums[biggestSumIndex]
#     sequenceIndexlst = [biggestSumIndex]
#     while sequences[biggestSumIndex] is not None:
#         sequenceIndexlst.append(sequences[biggestSumIndex])
#         biggestSumIndex = sequences[biggestSumIndex]
#     lst = []
#     for i in reversed(sequenceIndexlst):
#         lst.append(array[i])
#     return [biggestSum, lst]


# second iteration
# O(n^2) time | O(n) space
# def maxSumIncreasingSubsequence(array):
#     # Write your code here.
#     arrLength = len(array)
#     sums = array.copy()
#     sequences = [None for _ in range(arrLength)]
#     biggestSumIndex = 0
#     for i in range(arrLength):
#         for j in range(0, i):
#             if array[j] < array[i] and array[i] + sums[j] > sums[i]:
#                 sums[i] = array[i] + sums[j]
#                 sequences[i] = j
#         if sums[i] > sums[biggestSumIndex]:
#             biggestSumIndex = i
#
#     biggestSum = sums[biggestSumIndex]
#     maxSubSequenceInReverse = [biggestSumIndex]
#     while sequences[biggestSumIndex] is not None:
#         maxSubSequenceInReverse.append(sequences[biggestSumIndex])
#         biggestSumIndex = sequences[biggestSumIndex]
#
#     maxSubSequence = []
#     for i in reversed(maxSubSequenceInReverse):
#         maxSubSequence.append(array[i])
#     return [biggestSum, maxSubSequence]


# third iteration
# O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    n = len(array)
    sums = array[:]
    sequences = [None] * n
    max_idx = 0

    for i in range(n):
        for j in range(0, i):
            if array[j] < array[i] and array[i] + sums[j] > sums[i]:
                sums[i] = array[i] + sums[j]
                sequences[i] = j
        if sums[i] > sums[max_idx]:
            max_idx = i

    biggestSum = sums[max_idx]
    # Reconstruct the subsequence
    subsequence = [array[max_idx]]
    while sequences[max_idx] is not None:
        max_idx = sequences[max_idx]
        subsequence.append(array[max_idx])
    return [biggestSum, subsequence[::-1]]


print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))
