def isSwapNecessary(array, firstIdx, secondIdx, _dict):
    firstNumber = _dict[array[firstIdx]]
    secondNumber = _dict[array[secondIdx]]

    if firstNumber > secondNumber:
        return 1
    return 0


# O(n ^ 2) time and O(1) space
def threeNumberSort(array, order):
    # Write your code here.
    _dict = {}
    for _idx, orderElem in enumerate(order):
        _dict[orderElem] = _idx

    # implementing the selection sort algorithm
    for i in range(len(array)):
        smallest_number_idx = i
        for j in range(i + 1, len(array)):
            if isSwapNecessary(array, smallest_number_idx, j, _dict):
                smallest_number_idx = j
        if i != smallest_number_idx:
            array[smallest_number_idx], array[i] = array[i], array[smallest_number_idx]
    return array


array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
threeNumberSort(array, order)
