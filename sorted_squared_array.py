# def sortedSquaredArray(array):
#     # Write your code here.
#     _lst = []
#     while(len(array)):
#         _max = max(array)
#         _min = min(array)

#         if abs(_max)**2 > abs(_min)**2:
#             _lst.insert(0, abs(_max)**2)
#             array.remove(_max)
#         else:
#             _lst.insert(0, abs(_min)**2)
#             array.remove(_min)

#     return _lst


def sortedSquaredArray(array):
    # Write your code here.
    arr_len = len(array)
    _lst = [0] * arr_len
    start = 0
    end, _idx = arr_len - 1, arr_len - 1

    while start <= end:
        if abs(array[start])**2 >= abs(array[end])**2:
            _lst[_idx] = abs(array[start]) ** 2
            start += 1
        else:
            _lst[_idx] = abs(array[end]) ** 2
            end -= 1
        _idx -= 1
    return _lst


array = [-11, -3, -1, 1, 2, 3, 5, 6, 8, 9]
print(sortedSquaredArray(array))
