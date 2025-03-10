# O(n) time | O(1) space
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    numsLen = len(nums)
    if numsLen <= 1:
        return numsLen

    slowPointerIdx, fastPointerIdx = 0, 0
    while fastPointerIdx < numsLen:
        if nums[slowPointerIdx] != nums[fastPointerIdx]:
            slowPointerIdx += 1
            if slowPointerIdx != fastPointerIdx:
                nums[slowPointerIdx] = nums[fastPointerIdx]
        fastPointerIdx += 1
    return slowPointerIdx + 1


nums = [1, 1, 1, 2, 2, 4, 5, 6, 6, 6, 7]
print(removeDuplicates(nums))