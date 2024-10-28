# graph traversal problem
# depth-first or breadth-first search.
# O(w * h) time and O(w * h)
# where w and h are width and height of the matrix respectively.
def removeIslands(matrix):
    # Write your code here.
    # create a shadow matrix
    visited = [[0 for elem in row] for row in matrix]
    isIsland = [[0 for elem in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if the particular cell has already been visited,
            # no need to visit them again
            if visited[i][j] == 1:
                continue

            # if the cell value is 0,
            # no need to do any operations on it
            if matrix[i][j] == 0:
                visited[i][j] = 1
                continue

            markIsland(i, j, matrix, visited, isIsland)

    for i in range(len(isIsland)):
        for j in range(len(isIsland[0])):
            if isIsland[i][j] == 1:
                matrix[i][j] = 0

    return matrix


def markIsland(row_idx, col_idx, matrix, visited, isIsland):

    flag = 0
    islandMarker = []
    stack = [[row_idx, col_idx]]
    while stack:
        i, j = stack.pop()
        islandMarker.append([i, j])

        if visited[i][j] == 1:
            continue

        # if the cell value is 0,
        # no need to do any operations on it
        if matrix[i][j] == 0:
            visited[i][j] = 1
            continue

        visited[i][j] = 1

        if matrix[i][j] == 0 or i == 0 or j == 0 or i == len(matrix) - 1 or j == len(matrix[0]) - 1:
            flag = 1

        stack.extend(getEligibleCoord(i, j, matrix, visited))

    if flag == 0:
        for i, j in islandMarker:
            isIsland[i][j] = 1

    return None



def getEligibleCoord(i, j, matrix, visited):

    _lst = []
    eligibleCoord = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
    for row_idx, col_idx in eligibleCoord:
        if 0 <= row_idx < len(matrix) and 0 <= col_idx < len(matrix[0]):
            if visited[row_idx][col_idx] == 1:
                continue

            if matrix[row_idx][col_idx] == 0:
                visited[row_idx][col_idx] = 1
                continue

            _lst.append([row_idx, col_idx])
    return _lst


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]
removeIslands(matrix)
