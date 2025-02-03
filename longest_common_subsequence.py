# first iteration
# O(n * m * min(n * m)) time | O(n * m * min(n * m)) space
# where n and m are the lengths of str1 and str2 respectively.
# def longestCommonSubsequence(str1, str2):
#     # Write your code here.
#     array = [["" for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
#     for i in range(1, len(str1) + 1):
#         for j in range(1, len(str2) + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 array[i][j] = array[i - 1][j - 1] + str2[j - 1]
#             else:
#                 if len(array[i - 1][j]) > len(array[i][j - 1]):
#                     array[i][j] = array[i - 1][j]
#                 else:
#                     array[i][j] = array[i][j - 1]
#     return list(array[-1][-1])


# second iteration
# there is no need to for a two-dimensional array,
# just 2 rows are enough for this problem.
# O(n * m * min(n, m)) time | O(m * min(n, m)) space
# where n and m are the lengths of bigger and smaller input string respectively.
# def longestCommonSubsequence(str1, str2):
#     # identify the smallest string among the two
#     # get the largest string in variable "str1".
#     if len(str1) < len(str2):
#         str1, str2 = str2, str1
#
#     prev_row = ["" for _ in range(len(str2) + 1)]
#     current_row = ["" for _ in range(len(str2) + 1)]
#
#     for i in range(1, len(str1)+1):
#         for j in range(1, len(str2)+1):
#             if str1[i-1] == str2[j-1]:
#                 current_row[j] = prev_row[j-1] + str1[i-1]
#             else:
#                 if len(current_row[j-1]) > len(prev_row[j]):
#                     current_row[j] = current_row[j-1]
#                 else:
#                     current_row[j] = prev_row[j]
#         prev_row = current_row
#         current_row = ["" for _ in range(len(str2) + 1)]
#     return list(prev_row[-1])


# third iteration
# O(n*m) time and O(n*m) space
def longestCommonSubsequence(str1, str2):
    array = [[[None, 0, None, None] for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    # explanation for the array [None, 0, None, None]
    #  None - stands for the character that is common between row and column, and should be part of
    # longestCommonSequence(lcs)
    # 0 - The number of characters/size of that particular cell.
    # None - row index
    # None - column index
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                array[i][j] = [str1[i-1], array[i-1][j-1][1] + 1, i-1, j-1]
            else:
                if array[i-1][j][1] > array[i][j-1][1]:
                    array[i][j] = [None, array[i-1][j][1], i-1, j]
                else:
                    array[i][j] = [None, array[i][j-1][1], i, j-1]
    return formSequence(array)


def formSequence(array):
    row = len(array) - 1
    col = len(array[0]) - 1
    sequence = []

    while row != 0 and col != 0:
        currentCellContent = array[row][col]
        if currentCellContent[0] is not None:
            sequence.append(currentCellContent[0])
        row = currentCellContent[2]
        col = currentCellContent[3]
    return list(reversed(sequence))


str1 = "ZXVVYZW"
str2 = "XKYKZPW"
print(longestCommonSubsequence(str1, str2))
