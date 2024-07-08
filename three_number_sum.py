# first iteration
# n - number of elements in the array
# m - number of triplets in the array
# O() time | O() space
def threeNumberSum(array, targetSum):
    # Write your code here.
    _lst = []                                                                       # O(m) space
    for _idx, num in enumerate(array):                                              # O(n) time
        _arr = twoNumberSum(array, targetSum, num)                                  # O(m * n) time
        _lst.extend([_list for _list in _arr if _list not in _lst])                 # O(m) time
    _lst.sort()                                                                     # O(m log(m)) time
    return _lst


def twoNumberSum(array, targetSum, first_num):
    # Write your code here.
    _lst = []                                                                       # O(m) space
    for num in array:                                                               # O(n) time
        if num != first_num:
            required_num = targetSum - first_num - num
            if required_num in array and required_num not in [num, first_num]:
                arr_ = [first_num, num, required_num]
                arr_.sort()
                if arr_ not in _lst:                                                # O(m) time
                    _lst.append(arr_)
    return _lst


array = [12, 3, 1, 2, -6, 5, 0, -8, -1, 6]
targetSum = 0
print(threeNumberSum(array, targetSum))
