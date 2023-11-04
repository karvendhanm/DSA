"""
You  are given as input an unsorted array of n distinct numbers,  where n is a power of 2. Give an algorithm that
identifies the second-largest number in the array while using at most n - 2 + log2(n) comparisons.
"""


def find_2nd_biggest_number_v1(arr):
    """
    goal: to do only at most n - 2 + log2(n) comparisons.
    status: this function has 2n-3 comparisons, way short of the goal
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


def largest_and_smallest(num1, num2):
    """

    :param num1:
    :param num2:
    :return:
    """

    if num1 > num2:
        return num1, num2
    return num2, num1


def find_2nd_biggest_number_v2(arr):
    """
    refactoring the function find_2nd_biggest_number_v1
    :param arr: unsorted array of n distinct numbers
    :return: returns the second-biggest number.
    """

    if len(arr) <= 1:
        return None

    big1, big2 = largest_and_smallest(arr[0], arr[1])

    arr = arr[2:]
    while len(arr):

        if arr[0] > big2:
            big1, big2 = largest_and_smallest(big1, arr[0])
        arr.pop(0)

    return big2


find_2nd_biggest_number_v2([4, 5, 6, 7, 8, 9, 10, 11])


























