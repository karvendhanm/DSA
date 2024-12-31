# second iteration - clever solution (optimal time and space complexity)
# O(n) time and O(n) space
# def minRewards(scores):
#     if len(scores) == 1:
#         return 1
#
#     # Merely a pass from left to right
#     # and a pass from right to left.
#     rewardsList = [1] * len(scores)
#     for idx in range(1, len(scores)):
#         if scores[idx] > scores[idx-1]:
#             rewardsList[idx] = max(rewardsList[idx-1] + 1, rewardsList[idx])
#
#     for idx in reversed(range(len(scores)-1)):
#         if scores[idx] > scores[idx+1]:
#             rewardsList[idx] = max(rewardsList[idx+1] + 1, rewardsList[idx])
#
#     return sum(rewardsList)


# third iteration - naive solution (sub-optimal time complexity)
# O(n ^ 2) time and O(n) space
def minRewards(scores):
    if len(scores) == 1:
        return 1

    rewardsList = [1] * len(scores)
    for idx in range(1, len(scores)):
        if scores[idx] > scores[idx - 1]:
            rewardsList[idx] = max(rewardsList[idx - 1] + 1, rewardsList[idx])
        else:
            while idx > 0 and scores[idx] < scores[idx - 1]:
                rewardsList[idx - 1] = max(rewardsList[idx - 1], rewardsList[idx] + 1)
                idx -= 1
    return sum(rewardsList)


scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))

