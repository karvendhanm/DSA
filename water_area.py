def getBoundingRightWallIndex(index, heights):

    tankRightWallIndex = None
    tankRightWallHeight = 0

    for i in range(index + 1, len(heights)):
        if heights[i] > tankRightWallHeight:
            tankRightWallIndex = i
            tankRightWallHeight = heights[i]
            if heights[i] > heights[index]:
                break
    return tankRightWallIndex


def getWaterHoldingCapacity(tank, heights):

    leftIndex, rightIndex = tank

    leftWallHeight, rightWallHeight = heights[leftIndex], heights[rightIndex]

    distanceBetweenWalls = rightIndex - leftIndex - 1
    if leftWallHeight > rightWallHeight:
        leftWallHeight, rightWallHeight = rightWallHeight, leftWallHeight

    intermediateWallsHeight = 0
    for i in range(leftIndex + 1, rightIndex):
        intermediateWallsHeight += heights[i]

    return (leftWallHeight * distanceBetweenWalls) - intermediateWallsHeight


# first iteration
# O(n ^ 2) time and O(n) space
def waterArea(heights):
    # Write your code here.
    tanks = []
    leftIndex, totalWaterHoldingCapacity = 0, 0

    while leftIndex < len(heights) - 1:
        if heights[leftIndex] == 0:
            leftIndex += 1
            continue

        rightIndex = getBoundingRightWallIndex(leftIndex, heights)
        if rightIndex is None:
            break

        tanks.append([leftIndex, rightIndex])
        leftIndex = rightIndex

    for tank in tanks:
        totalWaterHoldingCapacity += getWaterHoldingCapacity(tank, heights)
    return totalWaterHoldingCapacity


heights = [0, 1, 0, 1, 0, 2, 0, 3]
print(waterArea(heights))
