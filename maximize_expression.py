# first iteration - brute force
# O(n^4) time | O(1) space
def maximizeExpression(array):
    # Write your code here.
    if len(array) < 4:
        return 0

    maxSum = float("-inf")
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                for l in range(k+1, len(array)):
                    maxSum = max(maxSum, array[i] - array[j] + array[k] - array[l])
    return maxSum


array = [3, 6, 1, -3, 2, 7]
print(maximizeExpression(array))
