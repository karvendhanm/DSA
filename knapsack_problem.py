# # first iteration
# # O(c * n) time | O(c * n) space
# # where c is the capacity of the knapsack
# # n is the number of items available
# def knapsackProblem(items, capacity):
#     # [value, itemIndex, row, col]
#     dp = [[[0, -1, -1, -1] for _ in range(capacity + 1)] for _ in range(len(items) + 1)]
# 
#     for i in range(1, len(items) + 1):
#         for w in range(1, capacity + 1):
#             if items[i - 1][1] <= w and items[i-1][0] + dp[i-1][w - items[i-1][1]][0] >= dp[i - 1][w][0]:
#                 dp[i][w][0] = items[i-1][0] + dp[i-1][w - items[i-1][1]][0]
#                 dp[i][w][1] = i - 1
#                 dp[i][w][2] = i - 1
#                 dp[i][w][3] = w - items[i-1][1]
#             else:
#                 dp[i][w][0] = dp[i - 1][w][0]
#                 dp[i][w][2] = i - 1
#                 dp[i][w][3] = w
#     return getSequence(dp)
# 
# 
# def getSequence(dp):
#     finalValue = dp[-1][-1][0]
#     index = dp[-1][-1][1]
#     indexes = []
# 
#     row, col = dp[-1][-1][2], dp[-1][-1][3]
#     while row != -1 or col != -1:
#         if index != -1:
#             indexes.append(index)
#         index = dp[row][col][1]
#         row, col = dp[row][col][2], dp[row][col][3]
#     return [finalValue, indexes[::-1]]


# second iteration
# O(c * n) time | O(c * n) space
# where c is the capacity of the knapsack
# n is the number of items available
def knapsackProblem(items, capacity):
    # [value, itemIndex, row, col]
    knapSackValues = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        currentWright = items[i - 1][1]
        currentValue = items[i - 1][0]
        for c in range(1, capacity + 1):
            if items[i - 1][1] <= c:
                knapSackValues[i][c] = max(knapSackValues[i - 1][c], currentValue + knapSackValues[i - 1][c - currentWright])
            else:
                knapSackValues[i][c] = knapSackValues[i - 1][c]
    return [knapSackValues[-1][-1], getKnapSackItems(knapSackValues, items)]


def getKnapSackItems(knapSackValues, items):
    sequence = []
    i = len(knapSackValues) - 1
    j = len(knapSackValues[0]) - 1

    while i > 0:
        if knapSackValues[i][j] != knapSackValues[i - 1][j]:
            sequence.append(i-1)
            j = j - items[i-1][1]
        i -= 1
        if knapSackValues[i][j] == 0:
            break
    return sequence[::-1]


items = [
    [1, 2],
    [4, 3],
    [5, 6],
    [6, 7]
]
capacity = 10
print(knapsackProblem(items, capacity))
