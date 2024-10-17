# first iteration
# O(n) time | O(1) space
def kadanesAlgorithm(array):
    # Write your code here.
    cumsum, max_sum = 0, 0
    for elem in array:
        cumsum += elem
        if cumsum <= 0:
            cumsum = max(0, elem)
        if cumsum > max_sum:
            max_sum = cumsum

    if max_sum == 0:    # this denotes a scenario where all the elements in the array are <= 0.
        for _idx, elem in enumerate(array):
            current = elem
            if current > max_sum or _idx == 0:
                max_sum = current

    return max_sum


array = [-10, -2, -9, -4, -8, -6, -7, -1, -3, -5]
print(kadanesAlgorithm(array))