# first iteration
# O(mn) time | O(m) + O(n) space
# where m - number of characters in "characters" string.
# where n - number of characters in "document" string.
# def generateDocument(characters, document):
#     # Write your code here.
#     if document == "":
#         return True
#
#     characters = list(characters)
#     document = list(document)
#
#     for _char in document:
#         if _char not in characters:
#             return False
#         characters.remove(_char)
#     return True


# O(m) + O(n) time | O(c) space
# where m - number of characters in "characters" string.
# where n - number of characters in "document" string.
# where c - number of unique characters in "characters" string.
# second iteration
def generateDocument(characters, document):
    # Write your code here.
    if document == "":
        return True

    char_dict = {}
    for _char in characters:
        if _char not in char_dict:
            char_dict[_char] = 0
        char_dict[_char] += 1

    for _char in document:
        if _char not in char_dict or char_dict[_char] <= 0:
            return False
        char_dict[_char] -= 1
    return True



characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"


generateDocument(characters, document)