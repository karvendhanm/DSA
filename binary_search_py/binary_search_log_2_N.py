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



def binary_search_recursion(_lst, elem):
    '''


    :param _lst: a sorted list of numerals
    :param elem: the element whose index needs to be found in the list: _lst
    :return: the index of the elem in the _lst
    :start_at:
    '''

    _len = len(_lst)
    _idx = int(_len/2) if _len % 2 == 0 else int((_len-1)/2)
    if _lst[_idx] != elem:
        if elem > _lst[_idx]:
            temp_idx = binary_search_recursion(_lst[_idx + 1:], elem)
            _idx += (temp_idx + 1)
        else:
            _idx = binary_search_recursion(_lst[:_idx], elem)

    return _idx


_lst = [11, 34, 46, 57, 61, 63, 78, 81, 85, 86, 87, 99]
elem_index = binary_search_grokking(_lst, 99)
print(elem_index)