# first iteration
# O(n) time | O(n) space
# where n is the length of the string
def reverseWordsInString(string):
    # Write your code here.
    strLength = len(string)
    reversedString = []
    EndPosition = strLength - 1
    previousCharacter = None
    for idx in range(strLength - 1, -1, -1):
        if idx == 0:
            rotateString(string, idx, EndPosition, reversedString)
        elif string[idx] == ' ' and previousCharacter != ' ':
            rotateString(string, idx + 1, EndPosition, reversedString)
            reversedString.append(' ')
            EndPosition = idx - 1
        elif string[idx] == ' ' and previousCharacter == ' ':
            reversedString.append(' ')
            EndPosition -= 1
        previousCharacter = string[idx]
    return "".join(reversedString)


def rotateString(string, start, end, reversedString):
    for i in range(start, end+1):
        reversedString.append(string[i])


string = 'AlgoExpert is the  best!'
print(reverseWordsInString(string))
