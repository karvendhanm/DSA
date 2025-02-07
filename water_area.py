# def getBoundingRightWallIndex(index, heights):
#
#     tankRightWallIndex = None
#     tankRightWallHeight = 0
#
#     for i in range(index + 1, len(heights)):
#         if heights[i] > tankRightWallHeight:
#             tankRightWallIndex = i
#             tankRightWallHeight = heights[i]
#             if heights[i] > heights[index]:
#                 break
#     return tankRightWallIndex
#
#
# def getWaterHoldingCapacity(tank, heights):
#
#     leftIndex, rightIndex = tank
#
#     leftWallHeight, rightWallHeight = heights[leftIndex], heights[rightIndex]
#
#     distanceBetweenWalls = rightIndex - leftIndex - 1
#     if leftWallHeight > rightWallHeight:
#         leftWallHeight, rightWallHeight = rightWallHeight, leftWallHeight
#
#     intermediateWallsHeight = 0
#     for i in range(leftIndex + 1, rightIndex):
#         intermediateWallsHeight += heights[i]
#
#     return (leftWallHeight * distanceBetweenWalls) - intermediateWallsHeight
#
#
# # first iteration
# # O(n ^ 2) time and O(n) space
# def waterArea(heights):
#     # Write your code here.
#     tanks = []
#     leftIndex, totalWaterHoldingCapacity = 0, 0
#
#     while leftIndex < len(heights) - 1:
#         if heights[leftIndex] == 0:
#             leftIndex += 1
#             continue
#
#         rightIndex = getBoundingRightWallIndex(leftIndex, heights)
#         if rightIndex is None:
#             break
#
#         tanks.append([leftIndex, rightIndex])
#         leftIndex = rightIndex
#
#     for tank in tanks:
#         totalWaterHoldingCapacity += getWaterHoldingCapacity(tank, heights)
#     return totalWaterHoldingCapacity


# second iteration
# # O(n) time and O(n) space
# def waterArea(heights):
#     # Water standing on any index depends on just 2 things
#     # 1) the tallest pillar to the left
#     # 2) the tallest pillar to the right
#
#     # finding the tallest pillar to the left
#     maxes = [0 for _ in range(len(heights))]
#     leftMax = 0
#     for i in range(len(heights)):
#         height = heights[i]
#         maxes[i] = leftMax
#         leftMax = max(leftMax, height)
#
#     rightMax = 0
#     for i in reversed(range(len(heights))):
#         height = heights[i]
#         maxes[i] = min(rightMax, maxes[i])
#         maxes[i] = max(0, maxes[i] - height)
#         rightMax = max(height, rightMax)
#
#     return sum(maxes)


# third iteration
# # O(n) time and O(1) space
def waterArea(heights):
    if not heights or len(heights) < 3:
        return 0

    left, right = 0, len(heights) - 1
    leftMax, rightMax = heights[left], heights[right]
    water = 0

    while left < right:
        if leftMax < rightMax:
            left += 1
            leftMax = max(leftMax, heights[left])
            water += max(0, leftMax - heights[left])
        else:
            right -= 1
            rightMax = max(rightMax, heights[right])
            water += max(0, rightMax - heights[right])
    return water


# heights = [0, 1, 0, 1, 0, 2, 0, 3]
heights = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
print(waterArea(heights))
