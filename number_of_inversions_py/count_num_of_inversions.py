from number_of_inversions_py.count_split_inversions import CountSplitInversions

def CountNumOfInversions(_arr):
    '''

    :param _arr:
    :return: returns the number of inversions
    '''

    # the number of inversions will be the sum of left inversion + right inversion + split inversion.
    # left inversion - the index i, j are at most n/2.
    # right inversion - the index i, j are strictly greater than n/2.
    # split inversion - the index i at most n/2 and index j strictly greater than n/2.

    _arr_length = len(_arr)
    # base case similar to the base case of merge sort.
    if _arr_length <= 1:
        return _arr, 0

    split_index = _arr_length // 2
    _left_arr = _arr[:split_index]
    _right_arr = _arr[split_index:]

    l, num_l = CountNumOfInversions(_left_arr)
    r, num_r = CountNumOfInversions(_right_arr)
    sorted_arr, num_split_inversions = CountSplitInversions(l, r)
    tot_num_inversions = num_l + num_r + num_split_inversions

    return sorted_arr, tot_num_inversions

if __name__ == '__main__':
    _arr = [5, 4, 6, 3, 2, 1]
    res = CountNumOfInversions(_arr)
    print(res)