def CountSplitInversions(arr1, arr2):
    '''

    :param arr1: the input array must be a sorted array
    :param arr2: the input array must be a sorted array
    :return:
    '''

    len_aar1 = len(arr1)
    len_arr2 = len(arr2)

    n = len_aar1 + len_arr2
    i, j = 0, 0
    _lst = []

    for k in range(n):

        if arr1[i] <= arr2[j]:
            _lst.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            _lst.append(arr2[j])
            j += 1

        if i > len_aar1 - 1:
            _lst.extend(arr2[j:])
            break
        elif j > len_arr2 - 1:
            _lst.extend(arr1[i:])
            break

    return _lst




if __name__ == "__main__":
    arr1, arr2 = [4, 5, 6], [1, 2, 3]
    res = CountSplitInversions(arr1, arr2)
    print(res)