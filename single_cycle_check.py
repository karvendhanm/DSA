# first iteration
# O(n) time | O(n) space
def hasSingleCycle(array):
    # Write your code here.
    arr_length = len(array)
    flags = [0 for x in range(arr_length)]

    pos = 0
    for _ in range(arr_length):
        pos += array[pos]

        if pos > arr_length - 1:
            quotient = pos // arr_length
            pos = pos - (quotient * arr_length)
        elif pos < 0:
            quotient = abs(pos // arr_length)
            pos = pos + (quotient * arr_length)

        if not 0 <= pos <= arr_length - 1 or flags[pos] == 1:
            return False

        flags[pos] += 1

    if sum(flags) == arr_length:
        return True

    return False


array = [10, 11, -6, -23, -2, 3, 88, 908, -26]
hasSingleCycle(array)
