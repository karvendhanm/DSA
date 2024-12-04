def getEligibleadjacentCells(rowIndex, colIndex, board):
    numRows = len(board)
    numCols = len(board[0])

    allAdjacentCells = [[rowIndex - 1, colIndex - 1], [rowIndex - 1, colIndex], [rowIndex - 1, colIndex + 1],
                        [rowIndex, colIndex - 1], [rowIndex, colIndex + 1],
                        [rowIndex + 1, colIndex - 1], [rowIndex + 1, colIndex], [rowIndex + 1, colIndex + 1]]
    eligibleAdjacentCells = []
    for row, col in allAdjacentCells:
        if 0 <= row <= (numRows - 1) and 0 <= col <= (numCols - 1):
            if board[row][col] == 'H' or board[row][col] == 'M':
                eligibleAdjacentCells.append([row, col])
    return eligibleAdjacentCells


# first iteration
# O() space | O() time
def revealMinesweeper(board, row, column):
    # Write your code here.
    # if the player has clicked right on the mine
    if board[row][column] == 'M':
        board[row][column] = 'X'
        return board

    eligibleAdjacentCells = getEligibleadjacentCells(row, column, board)
    recursionQue = []
    minesCount = 0
    for currentRow, currentCol in eligibleAdjacentCells:
        if board[currentRow][currentCol] == 'M':
            minesCount += 1
        elif board[currentRow][currentCol] == 'H':
            recursionQue.append([currentRow, currentCol])
    board[row][column] = str(minesCount)

    if minesCount == 0:
        for recursionRow, recursionCol in recursionQue:
            revealMinesweeper(board, recursionRow, recursionCol)
    return board


board = [
    ["H", "H", "H", "H", "M"],
    ["H", "H", "M", "H", "H"],
    ["H", "H", "H", "H", "H"],
    ["H", "H", "H", "H", "H"]
]
row = 3
column = 4
revealMinesweeper(board, row, column)
