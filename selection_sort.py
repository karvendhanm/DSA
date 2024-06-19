def swap(array, i, j):
    if i != j:
        array[i], array[j] = array[j], array[i]


# iteration one
# O(n ^ 2) time | O(1) space
# def selectionSort(array):
#     # Write your code here.
#
#     master_idx = 0
#     while master_idx < len(array) - 1:
#         small_num_idx = master_idx
#         for _idx in range(master_idx, len(array)):
#             if array[_idx] < array[small_num_idx]:
#                 small_num_idx = _idx
#
#         swap(array, master_idx, small_num_idx)
#         master_idx += 1
#     return array


# iteration 2
def selectionSort(array):
    # Write your code here.

    for i in range(len(array)):
        arg_min = min(range(i, len(array)), key=lambda x: array[x])
        swap(array, arg_min, i)
    return array
