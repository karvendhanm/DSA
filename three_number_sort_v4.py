# three number sort using bucket sort.
# O(n) time | O(1) space
# def threeNumberSort(array, order):
#     _dict = {}
#     for elem in order:
#         _dict[elem] = 0
#
#     for elem in array:
#         _dict[elem] += 1
#
#     _idx = 0
#     for i in order:
#         for _ in range(_dict[i]):
#             array[_idx] = i
#             _idx += 1
#     return array


def swap(array, firstIdx, secondIdx):
    array[firstIdx], array[secondIdx] = array[secondIdx], array[firstIdx]
    return


# O(n) time | O(1) space
def threeNumberSort(array, order):
    first_idx = 0
    for current_idx in range(len(array)):
        if array[current_idx] == order[0]:
            swap(array, current_idx, first_idx)
            first_idx += 1
    last_idx = len(array) - 1
    for current_idx in reversed(range(len(array))):
        if array[current_idx] == order[2]:
            swap(array, current_idx, last_idx)
            last_idx -= 1
    return array


array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
threeNumberSort(array, order)
