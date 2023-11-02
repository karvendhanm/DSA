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

    biggest_num, second_biggest_num = 0, 0
    n1 = arr[0]
    n2 = arr[1]

    if n1 > n2:
        biggest_num = n1
        second_biggest_num = n2
    else:
        biggest_num = n2
        second_biggest_num = n1

    for _idx in range(2, len(arr)):
        if arr[_idx] > biggest_num:
            second_biggest_num = biggest_num
            biggest_num = arr[_idx]
        elif arr[_idx] > second_biggest_num:
            second_biggest_num = arr[_idx]
    return second_biggest_num

