# first iteration
# O(n^2) time | O(n) space
# def minNumberOfJumps(array):
#     # Write your code here.
#     jumps = [float('inf') for i in range(len(array))]
#     jumps[0] = 0
#     for i in range(1, len(array)):
#         for j in range(0, i):
#             if array[j] + j >= i:
#                 jumps[i] = min(jumps[i], jumps[j] + 1)
#     return jumps[-1]


# second iteration
# O(n) time | O(1) space
def minNumberOfJumps(array):
    if len(array) <= 1:
        return 0

    maxReach, steps = array[0], array[0]
    jumps = 0

    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, array[i] + i)
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1


array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
print(minNumberOfJumps(array))
