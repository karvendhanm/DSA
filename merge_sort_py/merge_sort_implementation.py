from merge_sort_py.combining_2_sorted_array_in_increasing_order import merge_ascending

def merge_sort(arr):
    '''

    :param arr:
    :return:
    '''
    if len(arr) <= 1:
        return arr

    _lst = []
    _size = len(arr) // 2

    _left = arr[:_size]
    _right = arr[_size:]

    l = merge_sort(_left)
    r = merge_sort(_right)

    _merged = merge_ascending(l, r)
    return _merged


merge_sort([8, 5, 2, 9, 5, 6, 3])
