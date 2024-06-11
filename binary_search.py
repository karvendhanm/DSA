# O(log n) time | O(log n) space
#1st iteration
# def binarySearch(array, target, overall_idx=0):
#     # Write your code here.
#     current_idx = len(array)//2
#
#     if (array[current_idx] > target) & (len(array) > 1):
#         return binarySearch(array[:current_idx], target, overall_idx)
#     elif (array[current_idx] < target) & (len(array) > 1):
#         return binarySearch(array[current_idx:], target, overall_idx+current_idx)
#     elif array[current_idx] == target:
#         return overall_idx + current_idx
#     return -1


# iterative approach - 2nd iteration
# O(log n) time | O(1) space
def binarySearch(array, target):
    left_idx = 0
    right_idx = len(array)-1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if array[mid_idx] == target:
            return mid_idx
        elif array[mid_idx] > target:
            right_idx = mid_idx - 1
        elif array[mid_idx] < target:
            left_idx = mid_idx + 1

    return -1
