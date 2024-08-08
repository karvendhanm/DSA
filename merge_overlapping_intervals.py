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


# second iteration
# O(n log(n)) time | O(n) space.
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda x: x[0])                                  # O(nlog(n))    time
    result = [intervals[0]]                                             # O(n) space

    for interval in intervals[1:]:
        if result[-1][1] >= interval[0]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)

    return result


# third iteration
# O(n log(n)) time | O(n) space.
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    intervals.sort(key=lambda x: x[0])
    mergedIntervals = []
    currentInterval = intervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in intervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            mergedIntervals.append(nextInterval)
            currentInterval = nextInterval
    return mergedIntervals
