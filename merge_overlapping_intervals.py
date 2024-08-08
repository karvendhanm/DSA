# first iteration
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    mergedArray = []
    currentPrimaryIdx, currentSecondaryIdx = 0, 1
    while len(intervals):
        if len(intervals) > 1 and checkOverlap(intervals[currentPrimaryIdx], intervals[currentSecondaryIdx]):
            Array = mergeIntervals(intervals[currentPrimaryIdx], intervals[currentSecondaryIdx])
            intervals = [interval for interval in intervals if interval != intervals[currentPrimaryIdx]
                         and interval != intervals[currentSecondaryIdx]]
            currentPrimaryIdx, currentSecondaryIdx = 0, 1
            intervals.append(Array)
            continue

        if currentSecondaryIdx >= len(intervals) - 1:
            mergedArray.append(intervals[currentPrimaryIdx])
            intervals.remove(intervals[currentPrimaryIdx])
            currentPrimaryIdx, currentSecondaryIdx = 0, 0

        currentSecondaryIdx += 1

    return mergedArray


def checkOverlap(array1, array2):
    for elem in array1:
        if array2[0] <= elem <= array2[1]:
            return 1
    return 0


def mergeIntervals(array1, array2):
    if array1 == array2:
        return array1

    startNum = array1[0]
    if array2[0] < array1[0]:
        startNum = array2[0]

    endNum = array2[1]
    if array1[1] > array2[1]:
        endNum = array1[1]

    return [startNum, endNum]
