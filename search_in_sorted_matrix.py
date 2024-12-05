# O(w + h) time and O(1) space
# where w is the width of the matrix and h is the height of the matrix.
def searchInSortedMatrix(matrix, target):
    # Write your code here.
    row = 0
    col = len(matrix[0]) - 1
    while 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        if matrix[row][col] == target:
            return [row, col]
        elif matrix[row][col] < target:
            row = row + 1
        elif matrix[row][col] > target:
            col = col - 1
    return [-1, -1]


matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ]
target = 44
print(searchInSortedMatrix(matrix, target))
