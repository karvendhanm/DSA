# first iteration
# O(n) time |  O(1) space
def isPalindrome(string):
    # Write your code here.
    start_idx = 0
    end_idx = len(string) - 1

    while start_idx <= end_idx:
        if string[start_idx] != string[end_idx]:
            return False
        start_idx += 1
        end_idx -= 1
    return True
