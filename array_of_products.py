# first iteration
# O(n^2) time | O(n) space
# def arrayOfProducts(array):
#     # Write your code here.
#     product = []
#     for _idx, num in enumerate(array):
#         i = 0
#         prod = 1
#         while i < len(array):
#             if i != _idx:
#                 prod *= array[i]
#             i += 1
#         product.append(prod)
#     return product


# second iteration
# O(n) time | O(n) space
def arrayOfProducts(array):
    # Write your code here.
    leftSideProductArray = [1 for _ in range(len(array))]
    rightSideProductArray = [1 for _ in range(len(array))]

    # filling up leftSideProductArray
    product = 1
    for i in range(len(array)):
        leftSideProductArray[i] = product
        product *= array[i]

    # filling up rightSideProductArray
    product = 1
    for i in reversed(range(len(array))):
        rightSideProductArray[i] = product
        product *= array[i]

    result = []
    for i in range(len(array)):
        result.append(leftSideProductArray[i] * rightSideProductArray[i])

    return result
