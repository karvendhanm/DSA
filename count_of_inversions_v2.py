def countSplitInversions(leftArr, rightArr):
    leftArrLength = len(leftArr)
    rightArrLength = len(rightArr)
    combinedArrLength = leftArrLength + rightArrLength

    leftArrIdx = 0
    rightArrIdx = 0
    sortedArr = []
    numInversions = 0
    for k in range(combinedArrLength):
        if leftArr[leftArrIdx] <= rightArr[rightArrIdx]:
            sortedArr.append(leftArr[leftArrIdx])
            leftArrIdx += 1
        else:
            sortedArr.append(rightArr[rightArrIdx])
            numInversions += len(leftArr[leftArrIdx:])
            rightArrIdx += 1

        if leftArrIdx == leftArrLength:
            sortedArr.extend(rightArr[rightArrIdx:])
            break
        if rightArrIdx == rightArrLength:
            sortedArr.extend(leftArr[leftArrIdx:])
            break

    return sortedArr, numInversions


def countInversionsHelper(array):
    # Write your code here.
    if len(array) <= 1:
        return array, 0

    arrayLength = len(array)
    arraySplitLength = arrayLength // 2

    leftArr = array[:arraySplitLength]
    rightArr = array[arraySplitLength:]
    l_arr, l = countInversionsHelper(leftArr)
    r_arr, r = countInversionsHelper(rightArr)
    sorted_arr, numInversions = countSplitInversions(l_arr, r_arr)

    return sorted_arr, l + r + numInversions


# O(n log(n)) time | O(n) space
def countInversions(array):
    _, count = countInversionsHelper(array)
    return count


array = [1, 10, 2, 8, 3, 7, 4, 6, 5]
print(countInversions(array))
