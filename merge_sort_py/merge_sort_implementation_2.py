def combine_two_arrays(arr1, arr2):
    """

    :param arr1: list of numbers already arranged in ascending order
    :param arr2: list of numbers already arranged in ascending order
    :return:
    """

    lst = []
    k = len(arr1) + len(arr2)

    i, j = 0, 0
    for m in range(k):

        if i == len(arr1):
            lst.extend(arr2[j:])
            break
        elif j == len(arr2):
            lst.extend(arr1[i:])
            break

        if arr1[i] > arr2[j]:
            lst.append(arr2[j])
            j += 1
        else:
            lst.append(arr1[i])
            i += 1

    return lst

def merge_sort2(arr):
    """

    :param arr: list of numbers
    :return:
    """

    arr_len = len(arr)

    if arr_len <= 1:
        return arr

    left_arr = arr[:arr_len//2]
    right_arr = arr[arr_len//2:]

    left_ = merge_sort2(left_arr)
    right_ = merge_sort2(right_arr)

    sorted_arr = combine_two_arrays(left_, right_)

    return sorted_arr



