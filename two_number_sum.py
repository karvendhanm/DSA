# time complexity O(n**2)
# def twoNumberSum(array, targetSum):
#     """
#
#     :param array:
#     :param targetSum:
#     :return:
#     """
#     for idx, i in enumerate(array[:-1]):
#         for j in array[idx+1:]:
#             if i + j == targetSum:
#                 return [i, j]
#     return []


# time complexity O(n)
# degrees of freedom approach
# def twoNumberSum(array, targetSum):
#     """
#
#     :param array:
#     :param targetSum:
#     :return:
#     """
#     for x in array:
#         y = targetSum - x
#         if (x != y) & (y in array):
#             return [x, y]
#     return []


# algoexpert solution2
# time complexity O(n)
# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         potentialMatch = targetSum - num
#         if potentialMatch in nums:
#             return [potentialMatch, num]
#         else:
#             nums[num] = True
#     return []

# time complexity O(nlogn)
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] > targetSum:
            right -= 1
        else:
            left +=1
    return []




array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))

