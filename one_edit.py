# first iteration
# O(nm) time | O(nm) space - suboptimal space
# where n - length of the first string
# where m - length of the second string
# def oneEdit(stringOne, stringTwo):
#     # Write your code here.
#     edits = [[x for x in range(len(stringOne) + 1)] for _ in range(len(stringTwo) + 1)]
#     for i in range(len(stringTwo) + 1):
#         edits[i][0] = i
#     for i in range(len(stringTwo) + 1):
#         for j in range(1, len(stringOne) + 1):
#             if stringTwo[i - 1] == stringOne[j - 1]:
#                 edits[i][j] = edits[i - 1][j - 1]
#             else:
#                 edits[i][j] = min(edits[i - 1][j - 1], edits[i][j - 1], edits[i - 1][j]) + 1
#     return edits[-1][-1] <= 1


# # second iteration
# # O(nm) time | O(min(n, m)) space
# # where n - length of the first string
# # where m - length of the second string
# def oneEdit(stringOne, stringTwo):
#     # identify the smallest string
#     smallestString = LargestString = ""
#     small = stringOne if len(stringOne) < len(stringTwo) else stringTwo
#     big = stringOne if len(stringOne) >= len(stringTwo) else stringTwo
#     previousRow = [x for x in range(len(small) + 1)]
#     currentRow = [x for x in range(len(small) + 1)]
#     for rowIdx in range(1, len(big) + 1):
#         currentRow[0] = rowIdx
#         for colIdx in range(1, len(small) + 1):
#             if big[rowIdx - 1] == small[colIdx - 1]:
#                 currentRow[colIdx] = previousRow[colIdx - 1]
#             else:
#                 currentRow[colIdx] = min(previousRow[colIdx - 1],
#                                          previousRow[colIdx],
#                                          currentRow[colIdx - 1]) + 1
#         previousRow = currentRow[:]
#     return currentRow[-1] <= 1


# third iteration
# O(n) time | O(1) space
def oneEdit(stringOne, stringTwo):
    if len(stringOne) > len(stringTwo):
        stringOne, stringTwo = stringTwo, stringOne
    numberofChanges = 0
    if len(stringOne) == len(stringTwo):
        # potential replacement scenario
        for i in range(len(stringTwo)):
            if stringOne[i] != stringTwo[i]:
                numberofChanges += 1
    else:
        # could be addition or removal scenario
        if (len(stringTwo) - len(stringOne)) >= 2:
            return False

        i = 0
        for j in range(len(stringTwo)):
            if i < len(stringOne) and stringOne[i] == stringTwo[j]:
                i += 1
            else:
                numberofChanges += 1
    return numberofChanges <= 1


stringOne = "abcd"
stringTwo = "yabde"
print(oneEdit(stringOne, stringTwo))
