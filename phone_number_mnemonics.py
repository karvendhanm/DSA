integer2ButtonLetters = {
    '0': ['0'],
    '1': ['1'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


# first iteration
# recursive solution
# O(n * 4 ^ n) time | O(n * 4 ^ n) space
# def phoneNumberMnemonics(phoneNumber, idx=None):
#     # Write your code here.
#     if idx is None:
#         idx = len(phoneNumber) - 1
#     if idx < 0:
#         return [""]
#     phoneNumberCharacters = list(phoneNumber)
#     charAtIndex = phoneNumberCharacters[idx]
#     mnemonics = phoneNumberMnemonics(phoneNumber, idx - 1)
#     buttonLetters = integer2ButtonLetters.get(charAtIndex)
#     currentMnemonics = []
#     for mnemonic in mnemonics:
#         for letter in buttonLetters:
#             currentMnemonics.append(mnemonic + letter)
#     return currentMnemonics


# second iteration
# iterative solution
# O(n * 4 ^ n) time | O(n * 4 ^ n) space
# def phoneNumberMnemonics(phoneNumber):
#     phoneNumberCharacters = list(phoneNumber)
#     currentMnemonics = [""]
#     for character in phoneNumberCharacters:
#         mnemonics = currentMnemonics
#         currentMnemonics = []
#         for mnemonic in mnemonics:
#             for letter in integer2ButtonLetters.get(character):
#                 currentMnemonics.append(mnemonic + letter)
#     return currentMnemonics


# third iteration, recursive solution
# O(n * 4 ^ n) time | O(n * 4 ^ n) space
def phoneNumberMnemonics(phoneNumber):
    currentMnemonic = ["0"] * len(phoneNumber)
    mnemonicsFound = []

    phoneNumberMnemonicsHelper(0, phoneNumber, currentMnemonic, mnemonicsFound)
    return mnemonicsFound


def phoneNumberMnemonicsHelper(idx, phoneNumber, currentMnemonic, mnemonicsFound):
    if idx == len(phoneNumber):
        mnemonic = "".join(currentMnemonic)
        mnemonicsFound.append(mnemonic)
    else:
        numberAtIndex = phoneNumber[idx]
        letters = integer2ButtonLetters[numberAtIndex]
        for letter in letters:
            currentMnemonic[idx] = letter
            phoneNumberMnemonicsHelper(idx + 1, phoneNumber, currentMnemonic, mnemonicsFound)


phoneNumber = "7777"
print(phoneNumberMnemonics(phoneNumber))
