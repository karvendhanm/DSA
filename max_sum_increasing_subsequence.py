# O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    # Write your code here.
    arrLength = len(array)
    sums = array.copy()
    sequences = [None for _ in range(arrLength)]
    for i in range(arrLength):
        for j in range(0, i):
            if array[j] < array[i] and array[i] + sums[j] > sums[i]:
                sums[i] = array[i] + sums[j]
                sequences[i] = j
    biggestSumIndex = 0
    for idx, sum in enumerate(sums):
        if sum > sums[biggestSumIndex]:
            biggestSumIndex = idx
    biggestSum = sums[biggestSumIndex]
    sequenceIndexlst = [biggestSumIndex]
    while sequences[biggestSumIndex] is not None:
        sequenceIndexlst.append(sequences[biggestSumIndex])
        biggestSumIndex = sequences[biggestSumIndex]
    lst = []
    for i in reversed(sequenceIndexlst):
        lst.append(array[i])
    return [biggestSum, lst]


print(maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30]))
