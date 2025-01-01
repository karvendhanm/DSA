# first iteration
# O(n) time | O(n) space
def longestSubarrayWithSum(array, targetSum):
    totalSum = 0
    cumSumArray = [0]
    for num in array:
        totalSum += num
        cumSumArray.append(totalSum)

    # dictionary to reduce the time complexity of
    # checking membership.
    cumSumDict = {}
    for idx, num in enumerate(cumSumArray):
        if num not in cumSumDict:
            cumSumDict[num] = [idx]

    maxRange = float('-inf')
    startIdx, endIx = 0, 0
    for idx in reversed(range(len(cumSumArray))):
        if cumSumArray[idx] < targetSum:
            break

        match = cumSumArray[idx] - targetSum
        if match in cumSumDict:
            for index in cumSumDict[match]:
                if index >= idx:
                    break
                currentRange = (idx - 1) - index
                if currentRange > maxRange:
                    maxRange = currentRange
                    startIdx = index
                    endIx = idx - 1
    if maxRange != float('-inf'):
        return [startIdx, endIx]
    return []


array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
targetSum = 1
print(longestSubarrayWithSum(array, targetSum))