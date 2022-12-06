# binary search
# After a list or an array is sorted, binary search takes just log2(N) to find the element.

def binary_search(_lst, elem):
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
            temp_idx = binary_search(_lst[_idx + 1:], elem)
            _idx += (temp_idx + 1)
        else:
            _idx = binary_search(_lst[:_idx], elem)

    return _idx


_lst = [11, 34, 46, 57, 61, 63, 78, 81, 85, 86, 87, 99]
elem_index = binary_search(_lst, 199)
print(elem_index)