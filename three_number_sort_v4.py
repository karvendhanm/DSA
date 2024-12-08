# three number sort using bucket sort.
# O(n) time | O(1) space
def threeNumberSort(array, order):
    _dict = {}
    for elem in order:
        _dict[elem] = 0

    for elem in array:
        _dict[elem] += 1

    _idx = 0
    for i in order:
        for _ in range(_dict[i]):
            array[_idx] = i
            _idx += 1
    return array


array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
threeNumberSort(array, order)