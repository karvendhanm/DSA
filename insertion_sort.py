# first iteration
# def insertionSort(array):
#     # Write your code here.
#     sortedArrEndIdx = 0
#     while sortedArrEndIdx < len(array) - 1:
#         numToInsert = array[sortedArrEndIdx + 1]
#         insertUnSortedNumber(array, sortedArrEndIdx, numToInsert)
#         sortedArrEndIdx += 1
#     return array
#
#
# def insertUnSortedNumber(array, sortedArrEndIdx, numToInsert):
#     insertIdx = identifyIndexToInsert(array, sortedArrEndIdx, numToInsert)
#     if insertIdx <= sortedArrEndIdx:
#         for elem in range(sortedArrEndIdx, insertIdx-1, -1):
#             array[elem + 1] = array[elem]
#         array[insertIdx] = numToInsert
#
#
# def identifyIndexToInsert(array, sortedArrEndIdx, numToInsert):
#     for _idx in range(sortedArrEndIdx + 1):
#         if array[_idx] > numToInsert:
#             return _idx
#     return sortedArrEndIdx + 1


# second iteration
# O(N^2) time | O(1) space
def insertionSort(array):
    for _idx in range(len(array)):
        while _idx > 0 and array[_idx] < array[_idx - 1]:
            array[_idx-1], array[_idx] = array[_idx], array[_idx-1]
            _idx -= 1
    return array
