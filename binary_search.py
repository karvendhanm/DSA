def binarySearch(array, target, overall_idx=0):
    # Write your code here.
    current_idx = len(array)//2

    if (array[current_idx] > target) & (len(array) > 1):
        return binarySearch(array[:current_idx], target, overall_idx)
    elif (array[current_idx] < target) & (len(array) > 1):
        return binarySearch(array[current_idx:], target, overall_idx+current_idx)
    elif array[current_idx] == target:
        return overall_idx + current_idx
    return -1


array = [1, 5, 23, 111]
temp = binarySearch(array, 33)
print(temp)

array = [0, 1, 21, 33, 45, 46, 61, 71, 72, 73, 76]
temp = binarySearch(array, 76)
print(temp)
print('this is just for debugging purposes')
