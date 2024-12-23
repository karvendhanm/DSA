# first iteration
# O(n) time | O(n) space
# where n is the length of the string
# def reverseWordsInString(string):
#     # Write your code here.
#     strLength = len(string)
#     reversedString = []
#     EndPosition = strLength - 1
#     previousCharacter = ''
#     for idx in range(strLength - 1, -1, -1):
#         if string[idx] == ' ' and previousCharacter != ' ':
#             rotateString(string, idx + 1, EndPosition, reversedString)
#             reversedString.append(' ')
#             EndPosition = idx - 1
#         elif idx == 0:
#             rotateString(string, idx, EndPosition, reversedString)
#         elif string[idx] == ' ' and previousCharacter == ' ':
#             reversedString.append(' ')
#             EndPosition -= 1
#         previousCharacter = string[idx]
#     return "".join(reversedString)


# def rotateString(string, start, end, reversedString):
#     for i in range(start, end+1):
#         reversedString.append(string[i])


# second iteration
# O(n) time | O(n) space
# where n is the length of the string
# def reverseWordsInString(string):
#     wordList = []
#     startOfWordIdx = 0
#     for i in range(len(string)):
#         if string[i] == ' ':
#             wordList.append(string[startOfWordIdx:i])
#             startOfWordIdx = i
#         elif string[i] != ' ' and string[startOfWordIdx] == ' ':
#             wordList.append(" ")
#             startOfWordIdx += 1
#     wordList.append(string[startOfWordIdx:])
#
#     reverseList(wordList)
#     return ''.join(wordList)
#
#
# def reverseList(wordList):
#     start, end = 0, len(wordList) - 1
#     while start < end:
#         wordList[start], wordList[end] = wordList[end], wordList[start]
#         start += 1
#         end -= 1


# third iteration
# O(n) time | O(n) space
# where n is the length of the string
def reverseWordsInString(string):
    characters = [char for char in string]
    reverseStringInParts(characters, 0, len(characters) - 1)

    startOfWordIdx = 0
    previousIdxChar = ''
    for idx, char in enumerate(characters):
        if char == ' ':
            reverseStringInParts(characters, startOfWordIdx, idx-1)
            startOfWordIdx = idx + 1
        elif previousIdxChar == ' ':
            startOfWordIdx = idx
        previousIdxChar = char
    reverseStringInParts(characters, startOfWordIdx, len(characters) - 1)
    return "".join(characters)


def reverseStringInParts(string, startIdx, endIdx):
    while startIdx < endIdx:
        string[startIdx], string[endIdx] = string[endIdx], string[startIdx]
        startIdx += 1
        endIdx -= 1


string = "AlgoExpert is the best!"
res = reverseWordsInString(string)
