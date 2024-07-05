# first iteration
# def commonCharacters(strings):
#     # Write your code here.
#     length = len(strings)
#     letters = list(set(strings[0]))
#     _lst = [i for i in letters]
#
#     for letter in letters:
#         for i in range(1, length):
#             if letter not in strings[i] and letter in _lst:
#                 _lst.remove(letter)
#                 break
#     return _lst


# second iteration
def commonCharacters(strings):
    # Write your code here.
    length = len(strings)
    letters = list(set(strings[0]))
    final_lst = [letter for letter in letters]

    for i in range(1, length):
        for letter in letters:
            if letter not in strings[i] and letter in final_lst:
                final_lst.remove(letter)
        letters = [letter for letter in final_lst]
    return final_lst


# O(n * m) time - where n is the numbers of strings in the input list and m is the max. number of characters in a string
# O(s) space - where s is the number of unique characters in all the strings put together.
# third iteration
# def commonCharacters(strings):
#     # Write your code here.
#     _character_count = {}
#     for string in strings:
#         _lst = set(list(string))
#         for char in _lst:
#             if char not in _character_count:
#                 _character_count[char] = 1
#             else:
#                 _character_count[char] += 1
#     _lst = []
#     for key, val in _character_count.items():
#         if val == len(strings):
#             _lst.append(key)
#     return _lst
