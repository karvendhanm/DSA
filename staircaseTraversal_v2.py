# O(k ^ n) time | O(n) space
# where k is the maxSteps and
# n is the height.
# recursive method, worst time complexity
# def staircaseTraversal(height, maxSteps):
#     # Write your code here.
#     return numStepsToTop(height, maxSteps)
#
#
# def numStepsToTop(height, maxSteps):
#     if height <= 1:
#         return 1
#
#     numSteps = 0
#     for step in range(1, min(height, maxSteps) + 1):
#         numSteps += numStepsToTop(height - step, maxSteps)
#
#     return numSteps


# using memoization
# O(k * n) time | O(n) space
# where k is the maxSteps and
# n is the height.
# def staircaseTraversal(height, maxSteps):
#     # Write your code here.
#     return numStepsToTop(height, maxSteps, {0: 1, 1: 1})
#
#
# def numStepsToTop(height, maxSteps, memoize):
#     if height in memoize:
#         return memoize[height]
#
#     numSteps = 0
#     for step in range(1, min(height, maxSteps) + 1):
#         numSteps += numStepsToTop(height - step, maxSteps, memoize)
#
#     memoize[height] = numSteps
#
#     return numSteps


# using dynamic programming.
# the key idea is: there are only maxSteps number of ways to reach the top.
# if we know the number of ways to reach these steps we can simply add them.
# O(k * n) time | O(n) space
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    _lst = [0] * (height + 1)
    _lst[0] = _lst[1] = 1

    for i in range(2, height + 1):
        numSteps = 0
        for step in range(1, min(i, maxSteps) + 1):
            numSteps += _lst[i - step]
        _lst[i] = numSteps

    return _lst[height]





height = 5
maxSteps = 3
print(staircaseTraversal(height, maxSteps))
