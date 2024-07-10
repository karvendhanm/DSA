# first iteration
# O(n^2) time | O(1) space
# def smallestDifference(arrayOne, arrayTwo):
#     # Write your code here.
#     difference = float('inf')
#     _lst = []
#     for num1 in arrayOne:
#         for num2 in arrayTwo:
#             if abs(num1 - num2) < difference:
#                 difference = abs(num1 - num2)
#                 _lst = [num1, num2]
#     return _lst


# second iteration
# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()                                                                 # O(nlog(n)) time
    arrayTwo.sort()                                                                 # O(nlog(m)) time

    _lst = []
    difference = float('inf')
    _idx1, _idx2 = 0, 0
    while _idx1 <= len(arrayOne) - 1 and _idx2 <= len(arrayTwo) - 1:                # O(n + m) time
        if abs(arrayOne[_idx1] - arrayTwo[_idx2]) < difference:
            difference = abs(arrayOne[_idx1] - arrayTwo[_idx2])
            _lst = [arrayOne[_idx1], arrayTwo[_idx2]]

        if arrayOne[_idx1] > arrayTwo[_idx2]:
            _idx2 += 1
        elif arrayOne[_idx1] < arrayTwo[_idx2]:
            _idx1 += 1
        else:
            return _lst
    return _lst



arrayOne = [240, 124, 86, 111, 2, 84, 954, 27, 89]
arrayTwo = [1, 3, 954, 19, 8]
print(smallestDifference(arrayOne, arrayTwo))