def pointToString(point):
    if point[0] % 1 == 0 and point[1] % 1 == 0:
        point = [int(coordinate) for coordinate in point]
    return ','.join([str(coordinate) for coordinate in point])


# O(n ^ 2) time | O(n) space
def countSquares(points):
    pointsSet = set()
    for point in points:
        pointsSet.add(pointToString(point))

    count = 0
    for pointA in points:
        for pointB in points:
            if pointA == pointB:
                continue

            midPoint = [(pointA[0] + pointB[0])/2, (pointA[1] + pointB[1])/2]
            xDistanceFromMidPoint = pointA[0] - midPoint[0]
            yDistanceFromMidPoint = pointA[1] - midPoint[1]

            pointC = [midPoint[0] + yDistanceFromMidPoint, midPoint[1] - xDistanceFromMidPoint]
            pointD = [midPoint[0] - yDistanceFromMidPoint, midPoint[1] + xDistanceFromMidPoint]

            if pointToString(pointC) in pointsSet and pointToString(pointD) in pointsSet:
                count += 1
    return count / 4


points = [
    [1, 1],
    [0, 0],
    [-4, 2],
    [-2, -1],
    [0, 1],
    [1, 0],
    [-1, 4]
  ]
print(countSquares(points))
