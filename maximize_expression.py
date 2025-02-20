# first iteration - brute force
# O(n^4) time | O(1) space
# def maximizeExpression(array):
#     # Write your code here.
#     if len(array) < 4:
#         return 0
#
#     maxSum = float("-inf")
#     for i in range(len(array)):
#         for j in range(i+1, len(array)):
#             for k in range(j+1, len(array)):
#                 for l in range(k+1, len(array)):
#                     maxSum = max(maxSum, array[i] - array[j] + array[k] - array[l])
#     return maxSum


# # second iteration - dynamic programming
# # O(n) time | O(n) space
# def maximizeExpression(array):
#     if len(array) < 4:
#         return 0
#
#     max_A = [float("-inf")] * len(array)
#     max_A_B = [float("-inf")] * len(array)
#     max_A_B_C = [float("-inf")] * len(array)
#     max_A_B_C_D = [float("-inf")] * len(array)
#
#     max_A[0] = array[0]
#     for i in range(1, len(array)):
#         max_A[i] = max(max_A[i-1], array[i])
#
#     for i in range(1, len(array)):
#         max_A_B[i] = max(max_A_B[i-1], max_A[i-1] - array[i])
#
#     for i in range(2, len(array)):
#         max_A_B_C[i] = max(max_A_B_C[i-1], max_A_B[i-1] + array[i])
#
#     for i in range(3, len(array)):
#         max_A_B_C_D[i] = max(max_A_B_C_D[i-1], max_A_B_C[i-1]-array[i])
#
#     return max_A_B_C_D[-1]



# third iteration - cosmetic changes to the second iteration
# O(n) time | O(n) space
def maximizeExpression(array):
    if len(array) < 4:
        return 0

    max_A = [float("-inf")] * len(array)
    max_A_B = [float("-inf")] * len(array)
    max_A_B_C = [float("-inf")] * len(array)
    max_A_B_C_D = [float("-inf")] * len(array)

    max_A[0] = array[0]
    for i in range(1, len(array)-3):
        max_A[i] = max(max_A[i-1], array[i])

    for i in range(1, len(array)-2):
        max_A_B[i] = max(max_A_B[i-1], max_A[i-1] - array[i])

    for i in range(2, len(array)-1):
        max_A_B_C[i] = max(max_A_B_C[i-1], max_A_B[i-1] + array[i])

    for i in range(3, len(array)):
        max_A_B_C_D[i] = max(max_A_B_C_D[i-1], max_A_B_C[i-1]-array[i])

    return max_A_B_C_D[-1]


array = [3, 6, 1, -3, 2, 7]
print(maximizeExpression(array))
