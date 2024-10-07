# O(nd) time | O(n) space
# where n is the amount and d is the number of denominations
def numberOfWaysToMakeChange(n, denoms,):
    # Write your code here.
    ways = [0 for _ in range(n+1)]
    ways[0] = 1

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] = ways[amount] + ways[amount - denom]
    return ways[n]


n = 10
denoms = [1, 5, 10, 25]


print(numberOfWaysToMakeChange(n, denoms))
