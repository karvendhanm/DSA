def combineSortedArrays(leftArr, rightArr):
    leftArrLength = len(leftArr)
    rightArrLength = len(rightArr)
    combinedArrLength = leftArrLength + rightArrLength

    leftArrIdx = 0
    rightArrIdx = 0
    sortedArr = []
    for k in range(combinedArrLength):
        if leftArrIdx == leftArrLength:
            sortedArr.extend(rightArr[rightArrIdx:])
            break
        elif rightArrIdx == rightArrLength:
            sortedArr.extend(leftArr[leftArrIdx:])
            break

        if leftArr[leftArrIdx] <= rightArr[rightArrIdx]:
            sortedArr.append(leftArr[leftArrIdx])
            leftArrIdx += 1
        else:
            sortedArr.append(rightArr[rightArrIdx])
            rightArrIdx += 1

    return sortedArr


def mergeSortedArrays(arrays):
    # Write your code here.
    firstArr = []
    while arrays:
        secondArr = arrays.pop()
        firstArr = combineSortedArrays(firstArr, secondArr)
    return firstArr


arrays = [
    [1, 5, 9, 21],
    [-1, 0],
    [-124, 81, 121],
    [3, 6, 12, 20, 150]
  ]
print(mergeSortedArrays(arrays))