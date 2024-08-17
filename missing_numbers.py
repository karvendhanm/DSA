# O(n) time | O(n) space
# def missingNumbers(nums):
#     # Write your code here.
#     result = []
#     nums = set(nums)
#     for _idx in range(len(nums) + 2):
#         if _idx + 1 not in nums:
#             result.append(_idx + 1)
#     return result


# second iteration
# O(n) time | O(1) space
def missingNumbers(nums):
    # Write your code here.
    _length = len(nums) + 3
    nNumArr = [i for i in range(1, _length)]
    nNumSum = sum(nNumArr)
    numsSum = sum(nums)

    # when we find the average difference between these 2 arrays,
    # one of the missing number must be above the average and the other
    # one below the average.
    avgDiff = (nNumSum - numsSum)//2

    nNumBeforeAvgSum, nNumAfterAvgSum = 0, 0
    for i in nNumArr:
        if i <= avgDiff:
            nNumBeforeAvgSum += i
        else:
            nNumAfterAvgSum += i

    for i in nums:
        if i <= avgDiff:
            nNumBeforeAvgSum -= i
        else:
            nNumAfterAvgSum -= i

    return [nNumBeforeAvgSum, nNumAfterAvgSum]


nums = [1, 4, 3, 5]
print(missingNumbers(nums))
