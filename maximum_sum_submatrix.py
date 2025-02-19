# first iteration
# O(r * c * size ^ 2) time | O(1) space
# where r is the number of rows in the matrix
# where c is the number of columns in the matrix
# where size (submatrix dimension - it is always a square matrix)
def maximumSumSubmatrix(matrix, size):
    # Write your code here.
    maxSum = float("-inf")
    rowLength = len(matrix)
    colLength = len(matrix[0])

    for rowEndIndex in range(size - 1, rowLength):
        for colEndIndex in range(size-1, colLength):
            currentSum = 0
            rowStartIndex = rowEndIndex - (size-1)
            colStartIndex = colEndIndex - (size-1)
            for rowIndex in range(rowStartIndex, rowEndIndex+1):
                currentSum += sum(matrix[rowIndex][colStartIndex:colEndIndex+1])
            if currentSum > maxSum:
                maxSum = currentSum
    return maxSum


size = 2
matrix = [
    [5, 3, -1, 5],
    [-7, 3, 7, 4],
    [12, 8, 0, 0],
    [1, -8, -8, 2]
]
print(maximumSumSubmatrix(matrix, size))
