def merge_ascending(_left, _right):
    '''

    :param _left:
    :param _right:
    :return:
    '''
    i, j = 0, 0
    _lst = []

    for k in range(len(_left + _right)):

        if len(_left) and len(_right):
            if _left[i] <= _right[j]:
                _lst.append(_left[i])
                i += 1
            elif _right[j] <= _left[i]:
                _lst.append(_right[j])
                j += 1


        if i > len(_left) - 1:
            _lst.extend(_right[j:])
            break
        elif j > len(_right) - 1:
            _lst.extend(_left[i:])
            break

    return _lst

