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
