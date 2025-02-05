def getBoundingRightWallAtIndex(index, array):
    boundingRightWallIndex = None
    boundingRightWallHeight = 0
    for i in range(index + 1, len(array)):
        if array[i] > boundingRightWallHeight:
            boundingRightWallIndex = i
            boundingRightWallHeight = array[i]
            if array[i] > array[index]:
                break
    return boundingRightWallIndex


def getWaterHoldingCapacity(tank, heights):
    leftIndex, rightIndex = tank
    leftWallHeight = heights[leftIndex]
    rightWallHeight = heights[rightIndex]
    distanceBetweenWalls = rightIndex - leftIndex - 1
    if leftWallHeight > rightWallHeight:
        leftWallHeight, rightWallHeight = rightWallHeight, leftWallHeight
    intermediateWalls = 0
    for i in range(leftIndex + 1, rightIndex):
        intermediateWalls += heights[i]
    return (leftWallHeight * distanceBetweenWalls) - intermediateWalls


# first iteration
def waterArea(heights):
    # Write your code here.
    tanks = []
    leftIndex = 0
    while leftIndex < len(heights) - 1:
        if heights[leftIndex] == 0:
            leftIndex += 1
            continue
        rightIndex = getBoundingRightWallAtIndex(leftIndex, heights)
        if rightIndex is None:
            break
        tanks.append([leftIndex, rightIndex])
        leftIndex = rightIndex
    totalWaterHoldingCapacity = 0
    for tank in tanks:
        totalWaterHoldingCapacity += getWaterHoldingCapacity(tank, heights)
    return totalWaterHoldingCapacity


heights = [0, 1, 0, 1, 0, 2, 0, 3]
print(waterArea(heights))
