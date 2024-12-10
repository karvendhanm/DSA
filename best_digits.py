# first iteration
# O(n) time | O(n) space
def bestDigits(number, numDigits):
    canditateNumbers = []
    for i in range(len(number)):
        while canditateNumbers and int(number[i]) >= int(canditateNumbers[-1]) and numDigits:
            canditateNumbers.pop()
            numDigits -= 1
        canditateNumbers.append(number[i])
    return "".join(canditateNumbers[:len(number) - numDigits])


number = "321"
numDigits = 1
print(bestDigits(number, numDigits))
