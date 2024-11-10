# def countNumberofNegativeElements(matrix):
#     return sum([elem < 0 for sublist in matrix for elem in sublist if elem < 0])
#
#
# def isPositiveNumberInAdjacentNodes(i, j, matrix):
#     potentialNodes = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
#     for row, column in potentialNodes:
#         if 0 <= row < len(matrix) and 0 <= column < len(matrix[0]):
#             if matrix[row][column] > 0:
#                 return 1
#     return 0
#
#
# # first iteration
# # sub-optimal time and space
# def minimumPassesOfMatrix(matrix):
#     # Write your code here.
#     numPasses = 0
#     previousNumNegativeNumbers = float('inf')
#     currentNumNegativeNumbers = countNumberofNegativeElements(matrix)
#     newMatrix = [sublist[:] for sublist in matrix]
#     while previousNumNegativeNumbers > currentNumNegativeNumbers > 0:
#
#         for row in range(len(matrix)):
#             for width in range(len(matrix[0])):
#                 if matrix[row][width] < 0:
#                     if isPositiveNumberInAdjacentNodes(row, width, matrix):
#                         newMatrix[row][width] = matrix[row][width] * -1
#
#         matrix = [sublist[:] for sublist in newMatrix]
#         previousNumNegativeNumbers = currentNumNegativeNumbers
#         currentNumNegativeNumbers = countNumberofNegativeElements(matrix)
#         numPasses += 1
#
#     if currentNumNegativeNumbers != 0:
#         return -1
#     return numPasses


def isNegativeValuePresent(matrix):
    """

    :param matrix:
    :return:
    """
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False


def positiveElementsPosition(matrix):
    """

    :param matrix:
    :return:
    """
    position = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 0:
                position.append([row, col])
    return position


def getAdjacentElementPositions(row, col, matrix):
    """

    :param row:
    :param col:
    :param matrix:
    :return:
    """
    eligiblePositions = []
    if row > 0:
        eligiblePositions.append([row-1, col])
    if col > 0:
        eligiblePositions.append([row, col-1])
    if row < len(matrix)-1:
        eligiblePositions.append([row+1, col])
    if col < len(matrix[0])-1:
        eligiblePositions.append([row, col+1])

    return eligiblePositions



# second iteration
# O(w * h) time | O(w * h) space
# w - width of the matrix
# h - height of the matrix
def minimumPassesOfMatrix(matrix):
    # Write your code here.
    nextValuesQueue = positiveElementsPosition(matrix)

    numPasses = 0
    while nextValuesQueue:
        currentValueQueue = nextValuesQueue
        nextValuesQueue = []

        while currentValueQueue:
            row, col = currentValueQueue.pop(0)
            adjPosition = getAdjacentElementPositions(row, col, matrix)
            for adj_row, adj_col in adjPosition:
                if matrix[adj_row][adj_col] < 0:
                    nextValuesQueue.append([adj_row, adj_col])
                    matrix[adj_row][adj_col] = matrix[adj_row][adj_col] * -1

        numPasses += 1

    if isNegativeValuePresent(matrix):
        return -1
    return numPasses - 1


def isNegativeValuePresent(matrix):
    """

    :param matrix:
    :return:
    """
    for row in matrix:
        for value in row:
            if value < 0:
                return True
    return False


def positiveElementsPosition(matrix):
    """

    :param matrix:
    :return:
    """
    position = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 0:
                position.append([row, col])
    return position


def getAdjacentElementPositions(row, col, matrix):
    """

    :param row:
    :param col:
    :param matrix:
    :return:
    """
    eligiblePositions = []
    if row > 0:
        eligiblePositions.append([row-1, col])
    if col > 0:
        eligiblePositions.append([row, col-1])
    if row < len(matrix)-1:
        eligiblePositions.append([row+1, col])
    if col < len(matrix[0])-1:
        eligiblePositions.append([row, col+1])

    return eligiblePositions



# third iteration
# O(w * h) time | O(w * h) space
# w - width of the matrix
# h - height of the matrix
def minimumPassesOfMatrix(matrix):
    # Write your code here.
    queue = positiveElementsPosition(matrix)

    numPasses = 0
    while queue:
        numItems = len(queue)

        while numItems:
            row, col = queue.pop(0)
            adjPosition = getAdjacentElementPositions(row, col, matrix)
            for adj_row, adj_col in adjPosition:
                if matrix[adj_row][adj_col] < 0:
                    queue.append([adj_row, adj_col])
                    matrix[adj_row][adj_col] = matrix[adj_row][adj_col] * -1
            numItems -= 1
        numPasses += 1

    if isNegativeValuePresent(matrix):
        return -1
    return numPasses - 1