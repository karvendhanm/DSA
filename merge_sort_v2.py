def mergeSortedArrays(leftArr, rightArr):
    leftArrLength = len(leftArr)
    rightArrLength = len(rightArr)
    combinedArrLength = leftArrLength + rightArrLength

    leftArrIdx = 0
    rightArrIdx = 0
    sortedArr = []
    for k in range(combinedArrLength):
        if leftArr[leftArrIdx] <= rightArr[rightArrIdx]:
            sortedArr.append(leftArr[leftArrIdx])
            leftArrIdx += 1
        else:
            sortedArr.append(rightArr[rightArrIdx])
            rightArrIdx += 1

        if leftArrIdx == leftArrLength:
            sortedArr.extend(rightArr[rightArrIdx:])
            break
        elif rightArrIdx == rightArrLength:
            sortedArr.extend(leftArr[leftArrIdx:])
            break

    return sortedArr


# O(n log(n)) time | O(n) space
def mergeSort(array):
    # Write your code here.
    if len(array) <= 1:
        return array

    arrayLength = len(array)
    arraySplitLength = arrayLength // 2

    leftArr = array[:arraySplitLength]
    rightArr = array[arraySplitLength:]
    l = mergeSort(leftArr)
    r = mergeSort(rightArr)
    return mergeSortedArrays(l, r)


array = [8, 5, 2, 9, 5, 6, 3]
mergeSort(array)