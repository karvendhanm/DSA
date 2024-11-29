# O(t - s) time | O(t - s) space
# where t is the target and
# s is the startingHand
def blackjackProbability(target, startingHand):
    # Write your code here.
    memo = {}
    return round(calculateProbability(target, startingHand, memo), 3)


def calculateProbability(target, currentHand, memo):
    if currentHand in memo:
        return memo[currentHand]

    if currentHand > target:
        return 1

    if currentHand + 4 >= target:
        return 0

    totalProbability = 0
    for cardDrawn in range(1, 11):
        totalProbability += 0.1 * calculateProbability(target, currentHand + cardDrawn, memo)

    memo[currentHand] = totalProbability
    return memo[currentHand]


target = 21
startingHand = 13
blackjackProbability(target, startingHand)