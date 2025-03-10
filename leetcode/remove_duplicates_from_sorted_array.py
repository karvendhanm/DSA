# first iteration
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


# second iteration
# this iteration is more intuitive than the first
# O(n) time | O(1) space
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    insertAtIdx = 1
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[insertAtIdx] = nums[i]
            insertAtIdx += 1
    return insertAtIdx


nums = [1, 1, 1, 2, 2, 4, 5, 6, 6, 6, 7]
print(removeDuplicates(nums))