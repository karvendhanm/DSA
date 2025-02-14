# third iteration
# O(n ^ 3 + m) time | O(n + m) space
# where n is the length of pi
# where m is the size of numbers
# doing the second iteration in reverse (starting from the last character).
def numbersInPi(pi, numbers):
    # Write your code here.
    numbersSet = set(numbers)
    cache = {}
    for i in reversed(range(len(pi))):
        numbersInPiHelper(pi, numbersSet, cache, 0)
    return cache[0] if cache[0] != float("inf") else -1


def numbersInPiHelper(pi, numbersSet, cache, index):
    if index == len(pi):
        # this scenario is only possible when the
        # entire pi string is in the numbersSet.
        return -1

    if index in cache:
        return cache[index]

    minSplits = float("inf")
    for i in range(index, len(pi)):
        prefix = pi[index:i+1]
        if prefix in numbersSet:
            splits = numbersInPiHelper(pi, numbersSet, cache, i+1)
            minSplits = min(minSplits, splits + 1)
    cache[index] = minSplits
    return minSplits


pi = "3141592"
numbers =["3141", '5', '92', '9', '2', '31', '41592']
print(numbersInPi(pi, numbers))
