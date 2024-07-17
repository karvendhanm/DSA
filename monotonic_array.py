# O(n) time | O(n) space.
# def isMonotonic(array):
#     # Write your code here.
#     if len(array) <= 1:
#         return True
#
#     _lst = []                                                                       # O(n) space
#     for i in range(len(array) - 1):                                                 # O(n) time
#         _lst.append(array[i+1] - array[i])
#
#     if all(elem>= 0 for elem in _lst) or all(elem <= 0 for elem in _lst):           # O(n) time
#         return True
#
#     return False


# second iteration
# O(n) time | O(1) space.
def isMonotonic(array):

    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            isNonIncreasing = False
        if array[i] < array[i-1]:
            isNonDecreasing = False
    return isNonDecreasing or isNonIncreasing
