# O(n) time | O(1) space.
def isMonotonic(arr):
    """

    :param arr:
    :return:
    """
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            isNonIncreasing = False
        elif arr[i] < arr[i-1]:
             isNonDecreasing = False
    return isNonDecreasing or isNonIncreasing


# O(n) time | O(1) space.
def isMonotonic(array):
    if len(array) <= 1:
        return True

    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i-1]
            continue
        elif breaksDirection(direction, array[i-1], array[i]):
            return False
    return True


def breaksDirection(direction, startInt, endInt):
    diff = endInt - startInt
    if direction > 0:
        return diff < 0
    return diff > 0

