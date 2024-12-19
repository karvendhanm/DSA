# def is_palindrome(string, start_idx, end_idx):
#     return True if start_idx >= end_idx else (string[start_idx] == string[end_idx]
#                                               and is_palindrome(string, start_idx + 1, end_idx - 1))
#
#
# # first iteration
# # O(n^3) time | O(n) space
# def longestPalindromicSubstring(string):
#     # Write your code here.
#     start_idx = end_idx = 0
#     for i in range(len(string)):
#         for j in range(i, len(string)):
#             if string[i] == string[j] and is_palindrome(string, i, j):
#                 if (j - i) > (end_idx - start_idx):
#                     start_idx = i
#                     end_idx = j
#     return string[start_idx:end_idx+1]


# # second iteration
# # O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    longest = [0, 1]
    for i in range(1, len(string)):
        odd = getCurrentLongestPalindrome(string, i - 1, i + 1)
        even = getCurrentLongestPalindrome(string, i - 1, i)
        currentLongest = max(odd, even, key=lambda x: x[1] - x[0])
        longest = max(currentLongest, longest, key=lambda x: x[1] - x[0])
    return string[longest[0]:longest[1]]


def getCurrentLongestPalindrome(string, startIdx, endIdx):
    while startIdx >= 0 and endIdx < len(string):
        if string[startIdx] != string[endIdx]:
            break
        startIdx -= 1
        endIdx += 1
    return [startIdx+1, endIdx]


string = 'abaxyzzyxf'
print(longestPalindromicSubstring(string))
