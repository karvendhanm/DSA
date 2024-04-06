# def isValidSubsequence(array, sequence):
#     # Write your code here.
#     seq_len = len(sequence)
#     arr_len = len(array)
#     if seq_len > arr_len:
#         return False

#     seq_idx, arr_idx = 0, 0
#     for seq in sequence[seq_idx:]:
#         for arr in array[arr_idx:]:
#             arr_idx += 1
#             if seq == arr:
#                 seq_idx += 1
#                 break
#             if arr_idx > arr_len - 1:
#                 return False

#     if seq_idx == seq_len:
#         return True
#     return False


# def isValidSubsequence(array, sequence):
#     # Write your code here.
#     lst = []
#     arr_idx = 0
#     for seq in sequence:
#         for arr in array[arr_idx:]:
#             arr_idx += 1
#             if seq == arr:
#                 lst.append(arr)
#                 break

#     if lst == sequence:
#         return True
#     return False


def isValidSubsequence(array, sequence):
    # Write your code here.
    _lst = []
    for arr in array:
        if arr in sequence:
            _lst.append(arr)
            if len(_lst) == len(sequence):
                break

    if _lst == sequence:
        return True
    return False


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


print(isValidSubsequence(array, sequence))
