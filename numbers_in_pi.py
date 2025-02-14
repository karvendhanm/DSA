# first iteration
# O(n ^ 3) time | O(n + m) space
# where n is the length of pi
# where m is the size of numbers
def numbersInPi(pi, numbers):
    # Write your code here.
    favNumbers = {num: True for num in numbers}
    minSplits = dict()
    return numbersInPiHelper(pi, favNumbers, minSplits)


def numbersInPiHelper(pi, favNumbers, minSplits):
    if pi in favNumbers:
        return 0

    if pi in minSplits:
        return minSplits[pi]

    if len(pi) == 1:
        return 0 if pi in favNumbers else -1

    for i in range(1, len(pi)):
        prefix, suffix = pi[:i], pi[i:]
        if prefix in favNumbers:
            minSplits[suffix] = numbersInPiHelper(suffix, favNumbers, minSplits)
            if minSplits[suffix] != -1:
                if pi in minSplits and minSplits[pi] != -1:
                    minSplits[pi] = min(minSplits[pi], minSplits[suffix] + 1)
                else:
                    minSplits[pi] = minSplits[suffix] + 1
            else:
                minSplits[pi] = minSplits[pi] if pi in minSplits else -1
    return minSplits.get(pi, -1)


pi = "3141592653589793238462643383279"
numbers =["3141", "1512", "159", "793", "12412451", "8462643383279"]
print(numbersInPi(pi, numbers))
