# first iteration
# O(n ^ 2) time | O(n) space
# sub-optimal time complexity
def sunsetViews(buildings, direction):
    # Write your code here.
    if not buildings:
        return []

    indices = []
    _range = None
    if direction == "EAST":
        for currentBuildingIdx in range(len(buildings) - 1):
            for nextBuildingIdx in range(currentBuildingIdx + 1, len(buildings)):
                if buildings[currentBuildingIdx] <= buildings[nextBuildingIdx]:
                    break
                if nextBuildingIdx == len(buildings) - 1:
                    indices.append(currentBuildingIdx)
        indices.append(len(buildings) - 1)
    else:
        for currentBuildingIdx in reversed(range(1, len(buildings))):
            for nextBuildingIdx in range(currentBuildingIdx-1, -1, -1):
                if buildings[currentBuildingIdx] <= buildings[nextBuildingIdx]:
                    break
                if nextBuildingIdx == 0:
                    indices.append(currentBuildingIdx)
        indices.append(0)

    return sorted(indices)  # O(n log (n)) time complexity


buildings = [3, 5, 4, 4, 3, 1, 3, 2]
direction = 'EAST'
print(sunsetViews(buildings, direction))
