# first iteration
# O(n) time and O(n) space
def minRewards(scores):
    # Write your code here.
    if len(scores) == 1:
        return 1

    # Need to identify both peaks and valleys
    valleyPeakDict = {idx: 'S' for idx in range(len(scores))}       # O(n) time
    rewardDict = {}

    for idx in range(len(scores)):                                  # O(n) time
        getPeakOrValleyStatus(idx, scores, valleyPeakDict)

    for idx in range(len(scores)):                                  # O(n) time
        if valleyPeakDict[idx] == 'V':
            rewardDict[idx] = 1

            left = idx - 1
            right = idx + 1
            while left >= 0:
                rewardDict[left] = max(rewardDict.get(left, rewardDict[left + 1] + 1), rewardDict[left + 1] + 1)
                if valleyPeakDict[left] == 'P':
                    break
                left -= 1
            while right < len(scores):
                rewardDict[right] = max(rewardDict.get(right, rewardDict[right - 1] + 1), rewardDict[right - 1] + 1)
                if valleyPeakDict[right] == 'P':
                    break
                right += 1
    return sum(rewardDict.values())


def getPeakOrValleyStatus(idx, scores, valleyPeakDict):
    # this function works under the assumption that all values in the scores array is unique.
    if idx == 0:
        if scores[idx + 1] > scores[idx]:
            valleyPeakDict[idx] = 'V'
        else:
            valleyPeakDict[idx] = 'P'
    elif idx == len(scores) - 1:
        if scores[idx - 1] > scores[idx]:
            valleyPeakDict[idx] = 'V'
        else:
            valleyPeakDict[idx] = 'P'
    elif scores[idx - 1] > scores[idx] and scores[idx + 1] > scores[idx]:
        valleyPeakDict[idx] = 'V'
    elif scores[idx - 1] < scores[idx] and scores[idx + 1] < scores[idx]:
        valleyPeakDict[idx] = 'P'


scores = [1, 2, 3, 2, 1, 0, 1, 2, 3, 2, 1]
print(minRewards(scores))
