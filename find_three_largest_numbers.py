import numpy as np

# O(n) time | O(n) space
def findThreeLargestNumbers(array):
    # Write your code here.
    first_num, second_num, third_num = float('-inf'), float('-inf'), float('-inf')

    for num in array:
        if num > first_num:
            third_num = second_num
            second_num = first_num
            first_num = num
        elif num > second_num:
            third_num = second_num
            second_num = num
        elif num > third_num:
            third_num = num
    return [third_num, second_num, first_num]
