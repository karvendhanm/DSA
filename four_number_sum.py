# O(n ^ 3) time | O(n) space
# def fourNumberSum(array, targetSum):
#     # Write your code here.
#     quadraples = []
#     array.sort()
#     arrLength = len(array)
#     for firstIdx in range(arrLength - 3):
#         for secondIdx in range(firstIdx+1, arrLength - 2):
#             leftIdx = secondIdx + 1
#             rightIdx = arrLength - 1
#             while leftIdx < rightIdx:
#                 total = array[firstIdx] + array[secondIdx] + array[leftIdx] + array[rightIdx]
#                 if total == targetSum:
#                     quadraples.append([array[firstIdx], array[secondIdx], array[leftIdx], array[rightIdx]])
#                     leftIdx += 1
#                     rightIdx -= 1
#                 elif total < targetSum:
#                     leftIdx += 1
#                 elif total > targetSum:
#                     rightIdx -= 1
#     return quadraples


# second iteration
# O(n^2) time | O(n^2) space
def fourNumberSum(array, targetSum):
    two_number_sums = {}
    quadruplets = []
    for idx in range(len(array)):
        # first inner for loop that goes idx and forward
        for i in range(idx + 1, len(array)):
            tot_sum = array[idx] + array[i]
            wantedSum = targetSum - tot_sum
            if wantedSum in two_number_sums:
                for pairs in two_number_sums[wantedSum]:
                    quadruplets.append(pairs + [array[idx], array[i]])

        # second inner for loop that goes from first element to the idx element
        for j in range(0, idx):
            tot_sum = array[j] + array[idx]
            if tot_sum in two_number_sums:
                two_number_sums[tot_sum].append([array[j], array[idx]])
            else:
                two_number_sums[tot_sum] = [[array[j], array[idx]]]
    return quadruplets


array = [7, 6, 4, -1, 1, 2]
targetSum = 16
print(fourNumberSum(array, targetSum))























