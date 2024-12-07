def swap(array, idx, _dict):
    firstNumber = _dict[array[idx - 1]]
    secondNumber = _dict[array[idx]]

    if firstNumber > secondNumber:
        array[idx], array[idx - 1] = array[idx - 1], array[idx]
        return 1

    return 0


# first iteration
# O(n ^ 2) time | O(1) space
# sub-optimal time complexity
# def threeNumberSort(array, order):
#     # Write your code here.
#     _dict = {}
#     for _idx, orderElem in enumerate(order):
#         _dict[orderElem] = _idx
#
#     # implementing bubble sort
#     for i in range(len(array) - 1):
#         for j in range(1, len(array) - i):
#             swap(array, j, _dict)
#
#     return array


# second iteration
# O(n ^ 2) time | O(1) space
# sub-optimal time complexity
def threeNumberSort(array, order):
    # Write your code here.
    _dict = {}
    for _idx, orderElem in enumerate(order):
        _dict[orderElem] = _idx

    # implementing insertion sort
    for i in range(1, len(array)):
        while i > 0:
            if not swap(array, i, _dict):
                break
            i -= 1
    return array


array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
threeNumberSort(array, order)