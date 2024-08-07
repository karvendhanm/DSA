def mergeOverlappingIntervals(intervals):
    # Write your code here.
    mergedInterval = []
    currentPrimaryIdx, currentSecondaryIdx = 0, 1
    while len(intervals):
        if checkOverlap(intervals[currentPrimaryIdx], intervals[currentSecondaryIdx]):
            mergedArray = mergeIntervals(intervals[currentPrimaryIdx], intervals[currentSecondaryIdx])
            intervals.remove(intervals[currentPrimaryIdx])
            intervals.remove(intervals[currentSecondaryIdx])
            currentPrimaryIdx, currentSecondaryIdx = 0, 1
            mergedInterval.append(mergedArray)
        currentSecondaryIdx += 1
    return mergedInterval


def checkOverlap(array1, array2):
    for elem in array1:
        if array2[0] <= elem <= array2[1]:
            return 1
    return 0


def mergeIntervals(array1, array2):
    startNum = array1[0]
    if array2[0] < array1[0]:
        startNum = array2[0]

    endNum = array2[1]
    if array1[1] > array2[1]:
        endNum = array1[1]

    return [startNum, endNum]
