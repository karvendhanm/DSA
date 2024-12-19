def is_palindrome(string, start_idx, end_idx):
    return True if start_idx >= end_idx else (string[start_idx] == string[end_idx]
                                              and is_palindrome(string, start_idx + 1, end_idx - 1))


# first iteration
# O(n^3) time | O(n) space
def longestPalindromicSubstring(string):
    # Write your code here.
    longestPalindrome = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            if is_palindrome(string, i, j):
                if (j - i + 1) > len(longestPalindrome):
                    longestPalindrome = string[i:j+1]
    return longestPalindrome


string = 'abaxyzzyxf'
print(longestPalindromicSubstring(string))
