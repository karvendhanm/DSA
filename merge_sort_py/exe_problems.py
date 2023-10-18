import numpy as np

from merge_sort_py import merge_sort2


def min_gap(arr):
    """
    the parameter arr is an array of integers sorted in ascending order.
    :param arr:
    :return:
    """

    # sorting the array
    arr = merge_sort2(arr)
    min_num = float('inf')
    for _idx in range(0, len(arr) - 1):
        temp_num = arr[_idx + 1] - arr[_idx]
        if temp_num < min_num:
            min_num = temp_num

    if min_num == float('inf'):
        return None

    return min_num


def num_distinct_integers(arr):
    """

    :param arr:
    :return:
    """
    if len(arr) == 1:
        return 1

    # sorting the array
    arr = merge_sort2(arr)

    num_unique_numbers = 0
    for _idx in range(0, len(arr) - 1):
        if arr[_idx] != arr[_idx + 1]:
            num_unique_numbers += 1
    return num_unique_numbers


def deduplicate_array(arr):
    """

    :param arr:
    :return:
    """
    if len(arr) == 1 or len(arr) == 0:
        return arr

    # sorting the array
    arr = merge_sort2(arr)

    _lst = []
    for _idx in range(len(arr)):
        if arr[_idx] not in _lst:
            _lst.append(arr[_idx])
    return _lst


def find_modes(arr):
    """
    compute the mode. If there is a tie and there are multiple modes, return all of them.
    :param arr:
    :return:
    """

    # sorting the array
    arr = merge_sort2(arr)









