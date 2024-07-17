def isMonotonic(array):
    # Write your code here.
    if len(array) <= 1:
        return True

    _lst = []
    for i in range(len(array) - 1):
        _lst.append(array[i+1] - array[i])

    if len([True for elem in _lst if elem >= 0]) == len(array) - 1 or len([True for elem in _lst if elem <= 0]) == len(array) - 1:
        return True

    return False
