import math


def binary_search(array, target):
    '''

    :param array:
    :param target:
    :return:
    '''
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = math.floor((low + high)/2)
        guess = array[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def binary_search_recursion(array, target, low = 0, high = 0):
    '''

    :param array:
    :param target:
    :return:
    '''

    if low == 0 and high == 0:
        high = len(array) - 1

    mid = math.floor((low + high) / 2)
    guess = array[mid]

    if guess == target:
        return mid
    elif guess > target:
        tmp = binary_search_recursion(array, target, low=low, high=mid-1)
    else:
        tmp = binary_search_recursion(array, target, low=mid+1, high=high)

    if tmp != -1:
        return tmp

    return -1


print(binary_search_recursion([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
