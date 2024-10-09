# incorrect approach
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    ways = [-1 for _ in range(n + 1)]
    ways[0] = 0
    denoms.sort()

    for denom in denoms:
        for amount in range(1, n + 1):
            if amount >= denom:
                q = amount // denom
                r = amount % denom

                current = q + ways[r] if ways[r] != -1 else -1
                ways[amount] = min(ways[amount], current) if (current != -1 and ways[amount] != -1) else max(ways[amount], current)

    return ways[n]


n = 10
denoms = [1, 3, 4]

print(minNumberOfCoinsForChange(n, denoms))
