# first iteration
# O(n^2) time | O(n) space
# def longestPeak(array):
#     # Write your code here.
#     peakLength = [0]
#     for _idx in range(len(array) - 2):
#         peakStretch = _idx
#         valley = False
#
#         # upward slope
#         while peakStretch + 1 <= len(array) - 1 and array[peakStretch] < array[peakStretch + 1]:
#             peakStretch += 1
#
#         # downward slope
#         while (_idx < peakStretch and peakStretch + 1 <= len(array) - 1 and
#                array[peakStretch] > array[peakStretch + 1]):
#             valley = True
#             peakStretch += 1
#
#         if peakStretch >= _idx + 2 and valley:
#             peakLength.append(peakStretch - _idx + 1)
#
#     return max(peakLength)


# second iteration
# O(n) time | O(1) space
def longestPeak(array):
    # Write your code here.
    # finding peaks
    # peaks is a numbers with a strictly smaller number preceding as well as succeeding it,
    peakLength = 0
    _idx = 1
    while _idx < len(array) - 1:
        if array[_idx] > array[_idx - 1] and array[_idx] > array[_idx + 1]:
            peak = _idx

            # when a peak is found, establish the peak length
            # establish the starting point of the peak by going backwards
            peakStartingIndex = -1
            while _idx >= 1 and array[_idx] > array[_idx - 1]:
                peakStartingIndex = _idx - 1
                _idx -= 1
            _idx = peak

            # establish the ending point of a peak
            peakEndingIndex = -1
            while _idx <= len(array) - 2 and array[_idx] > array[_idx + 1]:
                peakEndingIndex = _idx + 1
                _idx += 1

            # two peaks could have a overlap of one number
            _idx -= 1

            if (peakEndingIndex - peakStartingIndex + 1) > peakLength:
                peakLength = peakEndingIndex - peakStartingIndex + 1

        _idx += 1

    return peakLength


array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))
