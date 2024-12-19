def is_palindrome(string, start_idx, end_idx):
    return True if start_idx >= end_idx else (string[start_idx] == string[end_idx]
                                              and is_palindrome(string, start_idx + 1, end_idx - 1))


# first iteration
# O(n^3) time | O(n) space
def longestPalindromicSubstring(string):
    # Write your code here.
    start_idx = end_idx = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i] == string[j] and is_palindrome(string, i, j):
                if (j - i) > (end_idx - start_idx):
                    start_idx = i
                    end_idx = j
    return string[start_idx:end_idx+1]


string = 'abaxyzzyxf'
print(longestPalindromicSubstring(string))
