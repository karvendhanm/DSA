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

    if len(arr) <= 1:
        return arr

    # sorting the array
    arr = merge_sort2(arr)

    mode_lst = []
    highest_freq = 0
    previous_elem = None
    for _idx, elem in enumerate(arr):

        if elem != previous_elem:
            current_elem_freq = 1
        else:
            current_elem_freq += 1

        if (current_elem_freq == highest_freq) & (elem not in mode_lst):
            mode_lst.append(elem)

        elif current_elem_freq > highest_freq:
            mode_lst = [elem]
            highest_freq += 1

        previous_elem = elem

    return mode_lst


def compute_median(arr):
    """

    :param arr: input array always has distinct integers and the length of the input array is odd.
    :return: median - number of other elements less than it equal to the number of elements greater than it.
    """

    if len(arr) <= 1:
        return arr

    # sorting the array
    arr = merge_sort2(arr)

    return arr[len(arr)//2]



    










