# first iteration
# O(n * m * min(n * m)) time | O(n * m * min(n * m)) space
# where n is the length of str2
# m is the length of str1
def longestCommonSubsequence(str1, str2):
    # Write your code here.
    array = [["" for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                array[i][j] = array[i - 1][j - 1] + str2[j - 1]
            else:
                if len(array[i - 1][j]) > len(array[i][j - 1]):
                    array[i][j] = array[i - 1][j]
                else:
                    array[i][j] = array[i][j - 1]
    return list(array[-1][-1])


str1 = "ZXVVYZW"
str2 = "XKYKZP"
print(longestCommonSubsequence(str1, str2))
