# O() time | O(h) space
# where h is the height of the staircase
# O(h) space as there will be maximum h number of frames in the call stack.
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    return staircaseTraversalHelper(height, maxSteps, 0)


def staircaseTraversalHelper(height, maxSteps, cnt):
    # base case
    if height <= 0:
        return cnt

    for step in range(1, maxSteps + 1):
        remainingHeight = height - step
        if remainingHeight == 0:
            cnt = cnt + 1
        cnt = staircaseTraversalHelper(remainingHeight, maxSteps, cnt)
    return cnt


height = 4
maxSteps = 2
print(staircaseTraversal(height, maxSteps))
