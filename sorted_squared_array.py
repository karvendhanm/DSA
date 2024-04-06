def sortedSquaredArray(array):
    # Write your code here.
    _lst = []
    while(len(array)):
        _max = max(array)
        _min = min(array)

        if abs(_max)**2 > abs(_min)**2:
            _lst.insert(0, abs(_max)**2)
            array.remove(_max)
        else:
            _lst.insert(0, abs(_min)**2)
            array.remove(_min)

    return _lst


array = [-11, -3, -1, 1, 2, 3, 5, 6, 8, 9]
print(sortedSquaredArray(array))
