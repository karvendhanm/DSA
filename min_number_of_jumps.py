# first iteration
# O(n^2) time | O(n) space
def minNumberOfJumps(array):
    # Write your code here.
    jumps = [float('inf') for i in range(len(array))]
    jumps[0] = 0
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
    return jumps[-1]


array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
print(minNumberOfJumps(array))
