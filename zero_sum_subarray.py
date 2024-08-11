# first iteration
# O(n^2) time | O(1) space
def zeroSumSubarray(nums):
    # Write your code here.
    for outer_idx, outer_elem in enumerate(nums):
        count = outer_elem
        if count == 0:
            return True
        for inner_idx in range(outer_idx+1, len(nums)):
            count += nums[inner_idx]
            if count == 0:
                return True
    return False


nums = [-5, -5, 2, 3, -2]
zeroSumSubarray(nums)
