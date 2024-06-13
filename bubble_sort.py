# first iteration
# O(n ** 2) time | O(1) space
def bubbleSort(array):
    # Write your code here.
    no_of_passes = len(array)
    for i in range(no_of_passes - 1):
        for j in range(no_of_passes - i - 1):
            if array[j + 1] < array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# second iteration
# O(n ** 2) time | O(1) space
def bubbleSort(array):
    _sorted = True
    counter = 0
    while _sorted:
        _sorted = False
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                _sorted = True
        counter += 1
    return array
