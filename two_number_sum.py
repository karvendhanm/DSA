# def twoNumberSum(array, targetSum):
#     """
#
#     :param array:
#     :param target_sum:
#     :return:
#     """
#     for idx, i in enumerate(array[:-1]):
#         for j in array[idx+1:]:
#             if i + j == targetSum:
#                 return [i, j]
#     return []


# degrees of freedom approach
def twoNumberSum(array, targetSum):
    """

    :param array:
    :param target_sum:
    :return:
    """
    for idx, x in enumerate(array):
        y = targetSum - x
        if (x != y) & (y in array):
            return [x, y]
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 244
print(two_number_sum(array, targetSum))