# when we need to reach from one point to another
# graphs should come to mind
# Also, the critical insight here is both the knights needn't move.
def getNextLocation(currentLocation, visitedSquares):
    x1, y1, distance = currentLocation
    xAxisMovement = [-2, 2, -1, 1, -2, 2, -1, 1]
    yAxisMovement = [-1, -1, -2, -2, 1, 1, 2, 2]
    nextLocations = []
    for x, y in zip(xAxisMovement, yAxisMovement):
        new_x, new_y = x1 + x, y1 + y
        if str([new_x, new_y]) in visitedSquares:
            continue
        nextLocations.append([new_x, new_y, distance + 1])
    return nextLocations


# O(n * m) time | O(n * m) space.
# where n is the horizontal distance between the 2 knights.
# where m is the horizontal distance between the 2 knights.
def knightConnection(knightA, knightB):
    # Write your code here.
    knightA.append(0)
    queue = [knightA]
    visitedSquares = set()
    while queue:
        currentPosition = queue.pop(0)
        *currentLocation, currentDistance = currentPosition
        if currentLocation == knightB:
            return int(currentDistance/2) if currentDistance % 2 == 0 else int(currentDistance/2) + 1

        if str(currentLocation) in visitedSquares:
            continue

        visitedSquares.add(str(currentLocation))
        nextLocations = getNextLocation(currentPosition, visitedSquares)
        queue.extend(nextLocations)
    return -1


knightA = [2, 1]
knightB = [0, 0]
print(knightConnection(knightA, knightB))