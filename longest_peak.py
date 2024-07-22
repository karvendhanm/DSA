# O(n^2) time | O(n) space
def longestPeak(array):
    # Write your code here.
    peakLength = [0]
    for _idx in range(len(array) - 2):
        peakStretch = _idx
        valley = False
        while peakStretch + 1 <= len(array) - 1 and array[peakStretch] < array[peakStretch + 1]:
            peakStretch += 1

        while (_idx < peakStretch and peakStretch + 1 <= len(array) - 1 and
               array[peakStretch] > array[peakStretch + 1]):
            valley = True
            peakStretch += 1

        if peakStretch >= _idx + 2 and valley:
            peakLength.append(peakStretch - _idx + 1)

    return max(peakLength)


array = []
print(longestPeak(array))
