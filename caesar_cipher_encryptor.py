# first iteration
# O(n) time | O(1) space
# def caesarCipherEncryptor(string, key):
#     # Write your code here.
#     alphabets = list("abcdefghijklmnopqrstuvwxyz")
#
#     _lst = []
#     for elem in string:
#         for _idx, char in enumerate(alphabets):
#             if char == elem:
#                 req_idx = _idx + key
#                 req_idx = req_idx if req_idx <= 25 else (req_idx % 26)
#                 _lst.append(alphabets[req_idx])
#                 break
#
#     return "".join(_lst)


# second iteration
# O(n) time | O(1) space
def caesarCipherEncryptor(string, key):
    # Write your code here.
    _lst = []
    for elem in string:
        num = ord(elem) + key
        num = (((num - 97) % 26) + 97) if num > 122 else num
        _lst.append(chr(num))
    return "".join(_lst)


string = 'xyz'
key = 2

print(caesarCipherEncryptor(string, key))
