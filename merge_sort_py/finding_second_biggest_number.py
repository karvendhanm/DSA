"""
You  are given as input an unsorted array of n distinct numbers,  where n is a power of 2. Give an algorithm that
identifies the second-largest number in the array while using at most n + log n (base 2) - 2 comparisons.
"""


def find_2nd_biggest_number(arr):
    """
    goal: to do only at most n + log n (base 2) - 2 comparisons.
    :param arr: unsorted array of n distinct numbers
    :return: returns the second-biggest number.
    """

    if len(arr) <= 1:
        return None

    biggest_num = arr[0]
    second_biggest_num = arr[1]

    if second_biggest_num > biggest_num:
        temp_var = biggest_num
        biggest_num = second_biggest_num
        second_biggest_num = temp_var

    for _idx in range(2, len(arr)):
        if arr[_idx] > biggest_num:
            second_biggest_num = biggest_num
            biggest_num = arr[_idx]
        elif arr[_idx] > second_biggest_num:
            second_biggest_num = arr[_idx]
    return second_biggest_num
