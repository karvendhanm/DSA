# first iteration
# O (n log(n)) time | O(1) space
# class Solution(object):
#     def removeElement(self, nums, val):
#         """
#         :type nums: List[int]
#         :type val: int
#         :rtype: int
#         """
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 nums[i] = float("inf")
#             else:
#                 k += 1
#         nums.sort()
#         return k


# second iteration
# O (n) time | O(1) space
# class Solution(object):
#     def removeElement(self, nums, val):
#         i = 0
#         n = len(nums) - 1
#         while i <= n:
#             if nums[i] == val:
#                 nums[i], nums[n] = nums[n], nums[i]
#                 n -= 1
#             else:
#                 i += 1
#         return n + 1


# third iteration
# O (n) time | O(1) space
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
obj = Solution()
print(obj.removeElement(nums, val))
