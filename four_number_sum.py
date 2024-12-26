# O(n ^ 3) time | O(n) space
def fourNumberSum(array, targetSum):
    # Write your code here.
    quadraples = []
    array.sort()
    arrLength = len(array)
    for firstIdx in range(arrLength - 3):
        for secondIdx in range(firstIdx+1, arrLength - 2):
            leftIdx = secondIdx + 1
            rightIdx = arrLength - 1
            while leftIdx < rightIdx:
                total = array[firstIdx] + array[secondIdx] + array[leftIdx] + array[rightIdx]
                if total == targetSum:
                    quadraples.append([array[firstIdx], array[secondIdx], array[leftIdx], array[rightIdx]])
                    leftIdx += 1
                    rightIdx -= 1
                elif total < targetSum:
                    leftIdx += 1
                elif total > targetSum:
                    rightIdx -= 1
    return quadraples
