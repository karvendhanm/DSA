# second iteration
# O(n) time | O(n) space
def bestSeat(seats):
    # Write your code here.
    if 0 not in seats:
        return -1

    leftArray = [0 for _ in seats]
    rightArray = [0 for _ in seats]

    # filling up the leftArray
    counter = -1
    for _idx, elem in enumerate(seats):
        if elem == 0:
            counter += 1
        elif elem == 1:
            counter = -1
        leftArray[_idx] = counter

    # filling up the rightArray
    counter = -1
    for _idx, elem in enumerate(reversed(seats)):
        if elem == 0:
            counter += 1
        elif elem == 1:
            counter = -1
        rightArray[len(seats) - 1 - _idx] = counter

    bestSeat = -1
    leftSideSpace = 0
    rightSideSpace = 0

    for _idx, (currLeftSide, currRightSide) in enumerate(zip(leftArray, rightArray)):
        if currRightSide != -1 and currLeftSide != -1:
            if (bestSeat == -1 or
                    (currLeftSide * currRightSide > leftSideSpace * rightSideSpace) or
                    (currRightSide > rightSideSpace and currLeftSide >= leftSideSpace) or
                    (currLeftSide > leftSideSpace and currRightSide >= rightSideSpace)):
                bestSeat = _idx
                leftSideSpace = currLeftSide
                rightSideSpace = currRightSide

    return bestSeat


seats = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
print(bestSeat(seats))
