# counting the number of inversions using brute force.

def count_num_inversions(arr):
    '''
    the problem with brute force is, the run time is quadratic O(n**2)
    :param _arr:
    :return:
    '''

    _num_inversions = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                _num_inversions += 1
    return _num_inversions


if __name__ == '__main__':
    res = count_num_inversions([4, 3, 6, 5, 1, 2])
    print(res)