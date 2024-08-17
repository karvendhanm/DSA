# O(n) time | O(n) space
def missingNumbers(nums):
    # Write your code here.
    result = []
    nums = set(nums)
    for _idx in range(len(nums) + 2):
        if _idx + 1 not in nums:
            result.append(_idx + 1)
    return result


nums = [1, 4, 3]
missingNumbers(nums)
