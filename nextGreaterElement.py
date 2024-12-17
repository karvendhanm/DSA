# first iteration
# O(n ^ 2) time | O(n) space
def nextGreaterElement(array):
    # Write your code here.
    result = [-1] * len(array)
    for idx, val in enumerate(array):
        for current_idx in range(idx + 1, idx + len(array)):
            current_idx = current_idx % len(array)
            if array[current_idx] > val:
                result[idx] = array[current_idx]
                break
    return result


array = [2, 5, -3, -4, 6, 7, 2]
nextGreaterElement(array)