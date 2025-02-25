# first iteration
# O(m +n) time | O(m) space
# suboptimal space. should be a constant space
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         temp = nums1[:m]
#         i, j = 0, 0
#         for k in range(m+n):
#             if i == m:
#                 while j != n:
#                     nums1[k] = nums2[j]
#                     k += 1
#                     j += 1
#                 break
#             elif j == n:
#                 while i != m:
#                     nums1[k] = temp[i]
#                     k += 1
#                     i += 1
#                 break
#
#             if temp[i] > nums2[j]:
#                 nums1[k] = nums2[j]
#                 j += 1
#             else:
#                 nums1[k] = temp[i]
#                 i += 1


# second iteration
# O(n + m) time | O(1) space
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         if n > 0:
#             for i in reversed(range(m + n)):
#                 if m == 0:
#                     while n > 0:
#                         nums1[i] = nums2[n-1]
#                         i -= 1
#                         n -= 1
#                 elif n == 0:
#                     while m > 0:
#                         nums1[i] = nums1[m - 1]
#                         i -= 1
#                         m -= 1
#                 else:
#                     if nums2[n - 1] > nums1[m - 1]:
#                         nums1[i] = nums2[n - 1]
#                         n -= 1
#                     else:
#                         nums1[i] = nums1[m - 1]
#                         m -= 1



# third iteration -  further refectoring the second iteration
# O(n + m) time | O(1) space
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m-1, n-1, m+n-1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
obj = Solution()
obj.merge(nums1, m, nums2, n)
