# first iteration
# O(n ^ 2) time | O(n) space
# sub-optimal time complexity
# def sunsetViews(buildings, direction):
#     # Write your code here.
#     if not buildings:
#         return []
#
#     indices = []
#     _range = None
#     if direction == "EAST":
#         for currentBuildingIdx in range(len(buildings) - 1):
#             for nextBuildingIdx in range(currentBuildingIdx + 1, len(buildings)):
#                 if buildings[currentBuildingIdx] <= buildings[nextBuildingIdx]:
#                     break
#                 if nextBuildingIdx == len(buildings) - 1:
#                     indices.append(currentBuildingIdx)
#         indices.append(len(buildings) - 1)
#     else:
#         for currentBuildingIdx in reversed(range(1, len(buildings))):
#             for nextBuildingIdx in range(currentBuildingIdx-1, -1, -1):
#                 if buildings[currentBuildingIdx] <= buildings[nextBuildingIdx]:
#                     break
#                 if nextBuildingIdx == 0:
#                     indices.append(currentBuildingIdx)
#         indices.append(0)
#
#     return sorted(indices)  # O(n log (n)) time complexity


# second iteration
# O(n) time | O(n) space
# def sunsetViews(buildings, direction):
#     maxHeight = 0
#     indices = []
#     _range = range(len(buildings)) if direction == 'WEST' else range(len(buildings) - 1, -1, -1)

#     for buildingIdx in _range:
#         if buildings[buildingIdx] > maxHeight:
#             indices.append(buildingIdx)
#             maxHeight = buildings[buildingIdx]
#     return indices if direction == 'WEST' else indices[::-1]


# third iteration
# O(n) time | O(n) space
# using a stack to solve this problem.
def sunsetViews(buildings, direction):
    # Write your code here.
    _range = range(len(buildings)) if direction == 'EAST' else range(len(buildings)-1, -1, -1)
    stack = []
    for idx in _range:
        while stack and buildings[idx] >= buildings[stack[-1]]:
            stack.pop()
        stack.append(idx)
    return stack if direction == 'EAST' else stack[::-1]


buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = 'WEST'
print(sunsetViews(buildings, direction))
