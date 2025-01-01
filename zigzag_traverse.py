def downMovement(rowIdx, colIdx, array, resultArray):
    rowLength = len(array)
    colLength = len(array[0])
    # do the down movement, if out of bounds do the horizontal movement
    if rowIdx + 1 < rowLength:
        resultArray.append(array[rowIdx+1][colIdx])
        rowIdx = rowIdx + 1
    elif colIdx + 1 < colLength:
        resultArray.append(array[rowIdx][colIdx + 1])
        colIdx = colIdx + 1
    return rowIdx, colIdx


def diagonalUpMovement(rowIdx, colIdx, array, resultArray):
    colLength = len(array[0])
    while rowIdx - 1 >= 0 and colIdx + 1 < colLength:
        resultArray.append(array[rowIdx - 1][colIdx + 1])
        rowIdx -= 1
        colIdx += 1
    return rowIdx, colIdx


def horizontalMovement(rowIdx, colIdx, array, resultArray):
    rowLength = len(array)
    colLength = len(array[0])
    # do the horizontal movement, if out of bounds do the down movement
    if colIdx + 1 < colLength:
        resultArray.append(array[rowIdx][colIdx + 1])
        colIdx = colIdx + 1
    elif rowIdx + 1 < rowLength:
        resultArray.append(array[rowIdx + 1][colIdx])
        rowIdx = rowIdx + 1
    return rowIdx, colIdx


def diagonalDownMovement(rowIdx, colIdx, array, resultArray):
    rowLength = len(array)
    while rowIdx + 1 < rowLength and colIdx - 1 >= 0:
        resultArray.append(array[rowIdx + 1][colIdx - 1])
        rowIdx += 1
        colIdx -= 1
    return rowIdx, colIdx


# first iteration
# O (l * b) time | O(l * b) space
# where l is the length of the array and
# b is the breadth of the array
def zigzagTraverse(array):
    # Write your code here.
    rowIdx, colIdx = 0, 0
    resultArray = [array[rowIdx][colIdx]]
    while not (rowIdx == len(array) - 1 and colIdx == len(array[0]) - 1):
        rowIdx, colIdx = downMovement(rowIdx, colIdx, array, resultArray)
        rowIdx, colIdx = diagonalUpMovement(rowIdx, colIdx, array, resultArray)
        rowIdx, colIdx = horizontalMovement(rowIdx, colIdx, array, resultArray)
        rowIdx, colIdx = diagonalDownMovement(rowIdx, colIdx, array, resultArray)
    return resultArray


# O(n) time | O(n) space
# where n is the total number of elements
# in the 2-dimensional array (height (h) * width (w))
def zigzagTraverse(array):
    rowIdx = columnIdx = 0
    zigzagArray = [array[rowIdx][columnIdx]]
    direction = 'down'
    while not (rowIdx == len(array)-1 and columnIdx == len(array[0])-1):
        if direction == 'down':
            direction = 'up'
            while rowIdx + 1 < len(array) and columnIdx - 1 >= 0:
                rowIdx = rowIdx + 1
                columnIdx = columnIdx - 1
                zigzagArray.append(array[rowIdx][columnIdx])
            # 2 special cases needs to be handled here for 'down' direction
            # case 1: when the indexes are at the 0th column.
            # case 2: when the indexes are at the last row.
            if rowIdx == len(array)-1 and columnIdx + 1 < len(array[0]):
                columnIdx = columnIdx + 1
                zigzagArray.append(array[rowIdx][columnIdx])
            elif columnIdx == 0 and rowIdx < len(array):
                rowIdx = rowIdx + 1
                zigzagArray.append(array[rowIdx][columnIdx])
        elif direction == 'up':
            direction = 'down'
            while rowIdx - 1 >= 0 and columnIdx + 1 < len(array[0]):
                rowIdx = rowIdx - 1
                columnIdx = columnIdx + 1
                zigzagArray.append(array[rowIdx][columnIdx])
            # 2 special cases needs to be handled here for 'up' direction
            # case 1: when the indexes are at the 0th row.
            # case 2: when the indexes are at the last column.
            if columnIdx == len(array[0])-1 and rowIdx + 1 < len(array):
                rowIdx = rowIdx + 1
                zigzagArray.append(array[rowIdx][columnIdx])
            elif rowIdx == 0 and columnIdx + 1 < len(array[0]):
                columnIdx = columnIdx + 1
                zigzagArray.append(array[rowIdx][columnIdx])
    return zigzagArray


array = [
    [1, 3, 4, 10],
    [2, 5, 9, 11],
    [6, 8, 12, 15],
    [7, 13, 14, 16]
]
print(zigzagTraverse(array))
