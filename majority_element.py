# note: this problem also has a bitwise operator solution.

# first iteration
# O(n^2) time | O(1) space
# def majorityElement(array):
#     # Write your code here.
#     # it is a non-empty, unordered array.
#     _length = len(array)
#     highestOccuringElement = None
#     highestOccuringElementCount = 0
#
#     for _outerIdx in range(_length):
#         count = 0
#         for _innerIdx in range(_outerIdx, _length):
#             if array[_innerIdx] == array[_outerIdx]:
#                 count += 1
#         if count > highestOccuringElementCount:
#             highestOccuringElementCount = count
#             highestOccuringElement = array[_outerIdx]
#             if highestOccuringElementCount >= (_length // 2) + 1:
#                 return highestOccuringElement


# second iteration
# O(n) time | O(1) space
def majorityElement(array):
    # Write your code here.
    _idx, startPointer = 0, 0
    score = 0
    while _idx < len(array):
        if array[_idx] == array[startPointer]:
            score += 1
        else:
            score -= 1

        _idx += 1

        if score == 0:
            startPointer = _idx
    if score > 0:
        return array[startPointer]


# third iteration
# refactoring the code
# O(n) time | O(1) space
def majorityElement(array):
    # Write your code here.
    _idx, startPointer = 1, 0
    score = 1
    while _idx < len(array):
        if array[_idx] == array[startPointer]:
            score += 1
        else:
            score -= 1

        _idx += 1

        if score == 0:
            startPointer = _idx
            score = 1
            _idx = _idx + 1
    if score > 0:
        return array[startPointer]


array = [1, 2, 3, 2, 2, 1, 2]
majorityElement(array)

