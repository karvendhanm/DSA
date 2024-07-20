import numpy as np

# this problem can be solved recursively
def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol+1):
            result.append(array[startRow][col])

        for row in range(startRow+1, endRow+1):
            result.append(array[row][endCol])

        # handle edge cases when there is only one column
        for col in reversed(range(startCol, endCol)):
            if startRow != endRow:
                result.append(array[endRow][col])

        # handle edge cases when there is only one row
        for row in reversed(range(startRow+1, endRow)):
            if startCol != endCol:
                result.append(array[row][startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result


array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6]
  ]
print(spiralTraverse(array))
