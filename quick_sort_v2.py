def quickSort(array):
    return quickSortHelper(array)


def quickSortHelper(array):
    if len(array) <= 1:
        return array

    pivotElem = array[0]
    leftArr = []
    pivotElemArr = []
    rightArr = []
    for elem in array:
        if elem < pivotElem:
            leftArr.append(elem)
        elif elem > pivotElem:
            rightArr.append(elem)
        else:
            pivotElemArr.append(elem)

    sortedLeftArr = quickSortHelper(leftArr)
    sortedrightArr = quickSortHelper(rightArr)

    return sortedLeftArr + pivotElemArr + sortedrightArr


array = [8, 3, 1, 7, 0, 10, 2]
print(quickSort(array))