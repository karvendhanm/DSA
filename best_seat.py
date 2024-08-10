# first iteration
# O(n^2) time | O(1) space
def bestSeat(seats):
    # Write your code here.
    if 0 not in seats:
        return -1

    bestSeat = -1
    leftSideSpace = 0
    rightSideSpace = 0

    for _idx, seat in enumerate(seats):
        if seat == 0:

            # determining left side free space
            fakeIndex = _idx
            currLeftSide = 0
            while fakeIndex - 1 > 0:
                if seats[fakeIndex - 1] == 1:
                    break
                currLeftSide += 1
                fakeIndex -= 1


            # determining right side free space
            fakeIndex = _idx
            currRightSide = 0
            while fakeIndex + 1 < len(seats) - 1:
                if seats[fakeIndex + 1] == 1:
                    break
                currRightSide += 1
                fakeIndex += 1

            # recalibrating the best seat
            if (bestSeat == -1 or
                    (currLeftSide * currRightSide > leftSideSpace * rightSideSpace) or
                    (currRightSide > rightSideSpace and currLeftSide >= leftSideSpace) or
                    (currLeftSide > leftSideSpace and currRightSide >= rightSideSpace)):
                bestSeat = _idx
                leftSideSpace = currLeftSide
                rightSideSpace = currRightSide

    return bestSeat


seats = [1, 0, 0, 0, 1, 0, 0, 0, 0, 1]
print(bestSeat(seats))
