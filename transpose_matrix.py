def transposeMatrix(matrix):
    # Write your code here.

    num_cols = len(matrix)
    num_rows = len(matrix[0])

    _lst = []
    for i in range(num_rows):
        _lst.append([0] * num_cols)

    for _idx, _list in enumerate(matrix):
        for list_idx, element in enumerate(_list):
            _lst[list_idx][_idx] = element

    return _lst


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transposeMatrix(matrix))
