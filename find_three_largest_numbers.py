import numpy as np

# O(n) time | O(n) space
# def findThreeLargestNumbers(array):
#     # Write your code here.
#     first_num, second_num, third_num = float('-inf'), float('-inf'), float('-inf')
#
#     for num in array:
#         if num > first_num:
#             third_num = second_num
#             second_num = first_num
#             first_num = num
#         elif num > second_num:
#             third_num = second_num
#             second_num = num
#         elif num > third_num:
#             third_num = num
#     return [third_num, second_num, first_num]

# O(n) time | O(n) space
# second iteration
def findThreeLargestNumbers(array):
    three_largest_nums = [float('-inf'), float('-inf'), float('-inf')]
    for num in array:
        threeLargestNumsUpdate(three_largest_nums, num)
    return three_largest_nums


def threeLargestNumsUpdate(three_largest_nums, num):
    if num > three_largest_nums[2]:
        shiftAndUpdate(three_largest_nums, num, 2)
    elif num > three_largest_nums[1]:
        shiftAndUpdate(three_largest_nums, num, 1)
    elif num > three_largest_nums[0]:
        shiftAndUpdate(three_largest_nums, num, 0)


def shiftAndUpdate(three_largest_nums, num, idx):
    for i in range(idx+1):
        if i == idx:
            three_largest_nums[i] = num
        else:
            three_largest_nums[i] = three_largest_nums[i+1]


array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
# output = []18, 141, 541

print(findThreeLargestNumbers(array))

