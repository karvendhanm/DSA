# O(n^2) time | O(1) space
def majorityElement(array):
    # Write your code here.
    # it is a non-empty, unordered array.
    _length = len(array)
    highestOccuringElement = None
    highestOccuringElementCount = 0

    for _outerIdx in range(_length):
        count = 0
        for _innerIdx in range(_outerIdx, _length):
            if array[_innerIdx] == array[_outerIdx]:
                count += 1
        if count > highestOccuringElementCount:
            highestOccuringElementCount = count
            highestOccuringElement = array[_outerIdx]
            if highestOccuringElementCount >= (_length // 2) + 1:
                return highestOccuringElement


array = [1, 2, 3, 2, 2, 1, 2]
majorityElement(array)
