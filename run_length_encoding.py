def runLengthEncoding(string):
    # Write your code here.
    letterLst, countLst = [], []
    previousLetter = ""
    cnt = 0
    for _idx, elem in enumerate(string):
        if _idx > 0 and (previousLetter != elem or cnt >= 9):
            letterLst.append(previousLetter)
            countLst.append(cnt)
            cnt = 0
        previousLetter = elem
        cnt += 1

    letterLst.append(string[-1])
    countLst.append(cnt)

    final_str = ""
    for cnt, alphabet in zip(countLst, letterLst):
        final_str += str(cnt) + alphabet
    return final_str


# second iteration
def runLengthEncoding(string):
    _idx, _newValIdx = 0, 0
    string = list(string)
    _str = ""
    while _newValIdx <= len(string)-1:
        _newValIdx += 1
        if _newValIdx == len(string) or string[_newValIdx] != string[_idx] or (string[_newValIdx] == string[_idx] and
                                                                               (_newValIdx - _idx) == 9):
            _str += str(_newValIdx - _idx) + string[_idx]
            _idx = _newValIdx
    return _str
