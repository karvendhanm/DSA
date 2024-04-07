from itertools import combinations


def nonConstructibleChange(coins):
    # Write your code here.
    if not len(coins):
        return 1

    for i in range(1, sum(coins)+2):
        for j in range(1, len(coins)+1):
            combs = list(combinations(coins, j))
            if i in list(set([sum(comb) for comb in combs])):
                break
            if j == len(coins):
                return i
