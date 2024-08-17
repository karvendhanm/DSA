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
# O(n) time | O(n) space
# def missingNumbers(nums):
#     # Write your code here.
#     _length = len(nums) + 3
#     # the below line of code is increasing space complexity from O(1) to O(n)
#     # better to keep recreating this array every single time it is needed if space is a constraint
#     nNumArr = [i for i in range(1, _length)]
#     nNumSum = sum(nNumArr)
#     numsSum = sum(nums)
#
#     # when we find the average difference between these 2 arrays,
#     # one of the missing number must be above the average and the other
#     # one below the average.
#     avgDiff = (nNumSum - numsSum)//2
#
#     nNumBeforeAvgSum = sum(range(1, avgDiff + 1))
#     nNumAfterAvgSum = sum(range(avgDiff + 1, _length))
#
#     for i in nums:
#         if i <= avgDiff:
#             nNumBeforeAvgSum -= i
#         else:
#             nNumAfterAvgSum -= i
#
#     return [nNumBeforeAvgSum, nNumAfterAvgSum]


# third iteration
def missingNumbers(nums):
    # Write your code here.
    _length = len(nums) + 3
    solutionXOR = 0
    for i in range(0, _length):
        solutionXOR ^= i

        if i < len(nums):
            solutionXOR ^= nums[i]

    solution = [0, 0]
    setBit = solutionXOR & -solutionXOR
    for i in range(0, _length):
        if i & setBit == 0:
            solution[0] ^= i
        else:
            solution[1] ^= i

        if i < len(nums):
            if nums[i] & setBit == 0:
                solution[0] ^= nums[i]
            else:
                solution[1] ^= nums[i]

    return sorted(solution)


nums = [1, 4, 3, 5]
print(missingNumbers(nums))
