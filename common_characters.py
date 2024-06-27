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
