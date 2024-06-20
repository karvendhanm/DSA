# first iteration
# O(n) time |  O(1) space
# def isPalindrome(string):
#     # Write your code here.
#     start_idx = 0
#     end_idx = len(string) - 1
#
#     while start_idx <= end_idx:
#         if string[start_idx] != string[end_idx]:
#             return False
#         start_idx += 1
#         end_idx -= 1
#     return True


# recursive way of solving the palindrome check.
# O(n) time |  O(n) space
# need to find out if slicing a string creates a new string.
# def isPalindrome(string):
#
#     if len(string) <= 1:
#         return True
#
#     if string[0] != string[-1]:
#         return False
#
#     return isPalindrome(string[1:-1])


# another way of writing the recursion without slicing a string
# O(n) time |  O(1) space
def isPalindrome(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)
