# O(n^2) time | O(1) time
# sub-optimal time complexity
def subarraySort(array):
    # Write your code here.
    # identifying smaller numbers going from the left:
    indices = [-1, -1]
    leftIndexFound = rightIndexFound = False
    for idx in range(len(array)):
        left = idx + 1
        while left < len(array):
            if array[left] < array[idx]:
                indices[0] = idx
                leftIndexFound = True
                break
            left += 1
        if leftIndexFound:
            break
    for idx in range(len(array)-1, -1, -1):
        right = idx - 1
        while right >= 0:
            if array[right] > array[idx]:
                indices[1] = idx
                rightIndexFound = True
                break
            right -= 1
        if rightIndexFound:
            break
    return indices


array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(array))