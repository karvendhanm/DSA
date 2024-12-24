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


# # third iteration
# # O(n) time | O(1) space
# # where n is the length of the larger among the two strings
# # here n being the length of the larger string is sub-optimal time complexity.
# def oneEdit(stringOne, stringTwo):
#     numberOfEdits = 0
#     if len(stringOne) == len(stringTwo):
#         # potential replacement scenario
#         for i in range(len(stringTwo)):
#             if stringOne[i] != stringTwo[i]:
#                 numberOfEdits += 1
#     else:
#         # potential addition or removal scenario
#         if len(stringOne) > len(stringTwo):
#             stringOne, stringTwo = stringTwo, stringOne
#
#         i = 0
#         for j in range(len(stringTwo)):
#             if i < len(stringOne) and stringOne[i] == stringTwo[j]:
#                 i += 1
#             else:
#                 numberOfEdits += 1
#     return numberOfEdits <= 1


# fourth iteration
# O(n) time | O(1) space
# where n is the length of the smaller string
def oneEdit(stringOne, stringTwo):
    lengthOne = len(stringOne)
    lengthTwo = len(stringTwo)
    if abs(lengthOne - lengthTwo) > 1:
        return False

    indexOne = 0
    indexTwo = 0
    madeEdit = False
    while indexOne < lengthOne and indexTwo < lengthTwo:
        if stringOne[indexOne] != stringTwo[indexTwo]:
            if madeEdit:
                return False
            madeEdit = True
            if lengthOne > lengthTwo:
                indexOne += 1
            elif lengthTwo > lengthOne:
                indexTwo += 1
            else:
                indexOne += 1
                indexTwo += 1
        else:
            indexOne += 1
            indexTwo += 1
    return True


stringOne = "abcd"
stringTwo = "yabde"
print(oneEdit(stringOne, stringTwo))
