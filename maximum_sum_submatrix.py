# # first iteration
# # O(r * c * size ^ 2) time | O(1) space
# # where r is the number of rows in the matrix
# # where c is the number of columns in the matrix
# # where size (submatrix dimension - it is always a square matrix)
# def maximumSumSubmatrix(matrix, size):
#     # Write your code here.
#     maxSum = float("-inf")
#     rowLength = len(matrix)
#     colLength = len(matrix[0])

#     for rowEndIndex in range(size - 1, rowLength):
#         for colEndIndex in range(size-1, colLength):
#             currentSum = 0
#             rowStartIndex = rowEndIndex - (size-1)
#             colStartIndex = colEndIndex - (size-1)
#             for rowIndex in range(rowStartIndex, rowEndIndex+1):
#                 currentSum += sum(matrix[rowIndex][colStartIndex:colEndIndex+1])
#             if currentSum > maxSum:
#                 maxSum = currentSum
#     return maxSum


# second iteration
# O(r * c) time | O(r * c) space
# where r is the number of rows in the matrix
# where c is the number of cols in the matrix
def maximumSumSubmatrix(matrix, size):
    # Write your code here.
    rowLength = len(matrix)
    colLength = len(matrix[0])

    prefixMatrix = [[0 for _ in range(colLength + 1)] for _ in range(rowLength + 1)]

    for i in range(rowLength):
        for j in range(colLength):
            prefixMatrix[i + 1][j + 1] = (matrix[i][j]
                                          + prefixMatrix[i + 1][j]
                                          + prefixMatrix[i][j + 1]
                                          - prefixMatrix[i][j])

    maxSum = float('-inf')
    for i in range(size, rowLength + 1):
        for j in range(size, colLength + 1):
            currentSum = (prefixMatrix[i][j]
                          + prefixMatrix[i-size][j-size]
                          - prefixMatrix[i-size][j]
                          - prefixMatrix[i][j-size])
            maxSum = max(maxSum, currentSum)

    return maxSum


size = 2
matrix = [
    [5, 3, -1, 5],
    [-7, 3, 7, 4],
    [12, 8, 0, 0],
    [1, -8, -8, 2]
]
print(maximumSumSubmatrix(matrix, size))
