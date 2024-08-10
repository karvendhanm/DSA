# third iteration
# O(n) time | O(1) space
def bestSeat(seats):
    # Write your code here.
    if 0 not in seats:
        return -1

    bestSeat_ = -1
    maxSpace = 0

    leftPointer, rightPointer = 0, 1
    while leftPointer < len(seats) - 1:
        if seats[rightPointer] == 1:
            distance = rightPointer - leftPointer
            if distance - 1 > maxSpace:
                maxSpace = distance - 1
                bestSeat_ = distance//2 + leftPointer
            leftPointer = rightPointer
        rightPointer += 1

    return bestSeat_


seats = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
print(bestSeat(seats))
