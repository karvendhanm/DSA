# second iteration
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


# third iteration
# O(n ^ 2) time and O(n) space
# def minRewards(scores):
#     if len(scores) == 1:
#         return 1
#
#     rewardsList = [1] * len(scores)
#     for idx in range(1, len(scores)):
#         if scores[idx] > scores[idx - 1]:
#             rewardsList[idx] = max(rewardsList[idx], rewardsList[idx - 1] + 1)
#         else:
#             while idx > 0 and scores[idx] < scores[idx - 1]:
#                 rewardsList[idx - 1] = max(rewardsList[idx - 1], rewardsList[idx] + 1)
#                 idx -= 1
#     return sum(rewardsList)


# fourth iteration
# O(n) time and O(n) space
# the method where we find peaks and valleys.
def minRewards(scores):
    if len(scores) == 1:
        return 1

    rewardsList = [1] * len(scores)
    for idx in range(len(scores)):
        if isValley(idx, scores):
            left = idx - 1
            right = idx + 1

            nextScore = scores[idx]
            while left >= 0 and scores[left] > nextScore:
                rewardsList[left] = max(rewardsList[left], rewardsList[left + 1] + 1)
                nextScore = scores[left]
                left -= 1

            previousScore = scores[idx]
            while right < len(scores) and scores[right] > previousScore:
                rewardsList[right] = max(rewardsList[right], rewardsList[right - 1] + 1)
                previousScore = scores[right]
                right += 1

    return sum(rewardsList)


def isValley(idx, scores):
    if idx == 0 and scores[idx] < scores[idx + 1]:
        return True
    elif idx == len(scores) - 1 and scores[idx] < scores[idx - 1]:
        return True

    if scores[idx] < scores[idx - 1] and scores[idx] < scores[idx + 1]:
        return True
    return False


scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))
