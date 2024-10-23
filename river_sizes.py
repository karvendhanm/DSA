# first iteration
# O(h.w) time and O(h.w) space
# where h is the height of the matrix
# where w is the width of the matrix
def riverSizes(matrix):
    # Write your code here.
    # this is a graph traversal algorithm
    # where depth-first or breadth-first search can be employed.
    # A shadow matrix to denote if a particular has been visited
    visited = [[0 for elem in row] for row in matrix]
    riverLengths = []
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            # if the particular node has already been visited, return back
            if visited[i][j]:
                continue
            # if the element at matrix is 0, then that means it is land
            # we simply mark that as visited and return back.
            if matrix[i][j] == 0:
                visited[i][j] = 1
                continue
            riverLengths.append(getRiverLength(i, j, matrix, visited))
    return riverLengths


def getRiverLength(i, j, matrix, visited):
    # Write your code here.
    riverLength = 0

    # Now we should look for unvisited adjacent nodes
    # to see if a river is present. we should do this
    # using a depth-first (stack) or breadth first (queue) approach.
    stack = [[i, j]] # will add eligible adjacent nodes to this stack.

    while stack:
        row_idx, col_idx = stack.pop()
        if visited[row_idx][col_idx]:
            continue

        if matrix[row_idx][col_idx] == 0:
            visited[row_idx][col_idx] = 1
            continue

        # here we have confirmed that this is an unvisited node
        # with a value of 1 -- a river.
        riverLength += 1
        visited[row_idx][col_idx] = 1

        stack.extend(getEligibleAdjacentNodes(row_idx, col_idx, matrix, visited))
    return riverLength


def getEligibleAdjacentNodes(i, j, matrix, visited):
    # Write your code here.
    eligibleNodes = []
    potentialNodes = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
    while potentialNodes:
        row_idx, col_idx = potentialNodes.pop()
        if 0 <= row_idx < len(visited) and 0 <= col_idx < len(visited[0]):
            if visited[row_idx][col_idx]:
                continue

            if matrix[row_idx][col_idx] == 0:
                visited[row_idx][col_idx] = 1
                continue

            eligibleNodes.append([row_idx, col_idx])
    return eligibleNodes


matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]
print(riverSizes(matrix))
