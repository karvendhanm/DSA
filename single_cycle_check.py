# first iteration
# O(n) time | O(n) space
def hasSingleCycle(array):
    # Write your code here.
    arr_length = len(array)
    flags = [0 for x in range(arr_length)]

    pos = 0
    for _ in range(arr_length):
        pos += array[pos]
        pos = pos % arr_length
        flags[pos] += 1

    return all(num == 1 for num in flags)


array = [2, 3, 1, -4, -4, 2]
hasSingleCycle(array)
