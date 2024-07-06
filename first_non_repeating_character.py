# O(n^2) time | O(c) space
# where n is the number of characters in the string
# where c is the number of unique characters in the string
# def firstNonRepeatingCharacter(string):
#     # Write your code here.
#     previously_seen = set()
#     for _idx, char in enumerate(string):
#         if char not in previously_seen:
#             scout = _idx + 1
#             while True:
#
#                 if scout > len(string) - 1:
#                     return _idx
#                 elif string[scout] == char:
#                     break
#
#                 scout += 1
#             previously_seen.add(char)
#     return -1


# O(n) time | O(1) space
# where n is the number of characters in the string
# this looks like O(c) space where c is the number of characters in the string
# However since the number of unique alphabets can't be more than 26, then O(26) = O(1)
def firstNonRepeatingCharacter(string):
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1

    for _idx, char in enumerate(string):
        if char_dict[char] == 1:
            return _idx

    return -1


string = "abab"
print(firstNonRepeatingCharacter(string))
