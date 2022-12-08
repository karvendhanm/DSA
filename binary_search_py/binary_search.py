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


print(binary_search([5, 23, 111], 3))
