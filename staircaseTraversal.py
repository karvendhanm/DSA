# O() time | O(h) space
# where h is the height of the staircase
# O(h) space as there will be maximum h number of frames in the call stack.
# def staircaseTraversal(height, maxSteps):
#     # Write your code here.
#     return staircaseTraversalHelper(height, maxSteps, 0)


# def staircaseTraversalHelper(height, maxSteps, cnt):
#     # base case
#     if height <= 0:
#         return cnt

#     for step in range(1, maxSteps + 1):
#         remainingHeight = height - step
#         if remainingHeight == 0:
#             cnt = cnt + 1
#         cnt = staircaseTraversalHelper(remainingHeight, maxSteps, cnt)
#     return cnt


# O(k ^ n) time | O(n) space
# def staircaseTraversal(height, maxSteps):
#     # Write your code here.
#     if height <= 1:
#         return 1
#
#     numWays = 0
#     for i in range(1, min(maxSteps, height) + 1):
#         numWays += staircaseTraversal(height - i, maxSteps)
#
#     return numWays


def numberOfStepsToTop(height, maxSteps, memoize):
    if height in memoize:
        return memoize[height]

    numWays = 0
    for i in range(1, min(maxSteps, height) + 1):
        numWays += numberOfStepsToTop(height - i, maxSteps, memoize)

    memoize[height] = numWays
    return numWays


# using memoization
# O(n * k) time | O(n) space
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return numberOfStepsToTop(height, maxSteps, {0:1, 1:1})


height = 4
maxSteps = 2
print(staircaseTraversal(height, maxSteps))
