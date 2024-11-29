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
# def staircaseTraversal(height, maxSteps):
#     # Write your code here.
#     waysToTop = [0 for _ in range(height + 1)]
#     waysToTop[0] = waysToTop[1] = 1
#
#     for currentHeight in range(2, height + 1):
#         numSteps = 0
#         for step in range(1, min(currentHeight, maxSteps) + 1):
#             numSteps += waysToTop[currentHeight - step]
#         waysToTop[currentHeight] = numSteps
#
#     return waysToTop[height]



# using dynamic programming.
# the key idea is: there are only maxSteps number of ways to reach the top.
# if we know the number of ways to reach these steps we can simply add them.
# O(k * n) time | O(n) space
# another interesting while loop for the same dynamic programming as listed above.
# def staircaseTraversal(height, maxSteps):
#     # Write your code here.
#     waysToTop = [0 for _ in range(height + 1)]
#     waysToTop[0] = waysToTop[1] = 1
#
#     for currentHeight in range(2, height + 1):
#         step = 1
#         while step <= maxSteps and step <= currentHeight:
#             waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight - step]
#             step += 1
#
#     return waysToTop[height]


# sliding window approach
# O(n) time | O(n) space
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    currentNumberOfWays = 0
    waysToTop = [1]

    for currentHeight in range(1, height+1):
        startOfWindow = currentHeight - maxSteps -1
        endOfWindow = currentHeight - 1

        if startOfWindow >= 0:
            currentNumberOfWays -= waysToTop[startOfWindow]

        currentNumberOfWays += waysToTop[endOfWindow]
        waysToTop.append(currentNumberOfWays)

    return waysToTop[height]


height = 5
maxSteps = 3
print(staircaseTraversal(height, maxSteps))
