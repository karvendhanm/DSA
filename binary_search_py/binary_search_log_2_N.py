# binary search
# After a list or an array is sorted, binary search takes just log2(N) to find the element.
import math


def binary_seach(_lst, item):
    '''

    :param _lst: A sorted list of elements, binary search works only if the list is sorted.
    :param item: the number whose index needs to be identified in the list(_lst).
    :return: index of the item in the list(_lst).
    '''
    if item not in _lst:
        return None

    low = 0
    high = len(_lst) - 1

    while low != high:

        mid = math.floor((low + high) / 2)
        guess = _lst[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return mid

    return low


def binary_search_grokking(array, target):
    '''

    :param array:
    :param target:
    :return:
    '''

    low = 0
    high = len(_lst) - 1

    while low <= high:
        mid = math.floor((low + high)/2)
        guess = array[mid]

        if guess > target:
            high = mid - 1
        elif guess < target:
            low = mid + 1
        else:
            return mid

    return None


_lst = [11, 34, 46, 57, 61, 63, 78, 81, 85, 86, 87, 99]
elem_index = binary_search_grokking(_lst, 99)
print(elem_index)